import unittest
from unittest.mock import patch, mock_open
from business_logic import get_most_popular_genres
from data_logic import check_input_file, load_data
from datetime import datetime


class TestBusinessLogic(unittest.TestCase):

    @patch('builtins.open', mock_open(read_data='tconst\ttitleType\tprimaryTitle\toriginalTitle\tyear\n'))
    def test_get_most_popular_genres_with_valid_year(self):
        # Test for getting most popular genres for a valid year
        expected_result = [{"count": 5727,"genres": "Drama"}]
        result = get_most_popular_genres('2022', 1)
        self.assertEqual(result, expected_result)

    def test_get_most_popular_genres_with_invalid_year_type(self):
        # Test for getting most popular genres for an invalid year type
        expected_result = {'error': 'Year parameter must be an integer'}, 400
        result = get_most_popular_genres('abcd', 1)
        self.assertEqual(result, expected_result)

    def test_get_most_popular_genres_with_year_out_of_range(self):
        # Test for getting most popular genres for a year out of range
        current_year = datetime.now().year
        expected_result = {'error': f'Year parameter must be between 1885 and {current_year}.'}, 400
        result = get_most_popular_genres(2030, 1)
        print('result', result)
        print('expected_result', expected_result)
        self.assertEqual(result, expected_result)

    def test_get_most_popular_genres_with_no_genres(self):
        # Test for getting most popular genres for a year with no available genres
        expected_result = {'error': 'No data found for year 1886.'}, 404
        result = get_most_popular_genres(1886, 10)
        self.assertEqual(result, expected_result)

    # @patch('builtins.open', side_effect=FileNotFoundError('test error'))
    # def test_get_most_popular_genres_with_missing_input_file(self, mock_open):
    #     # Test for getting most popular genres for a year with missing input file
    #     input_file = 'movies.tsv'
    #     expected_result = {'error': f'Error reading input file {input_file}.'}, 500
    #     result = get_most_popular_genres('2022', 1)
    #     self.assertEqual(result, expected_result)

    # @patch('builtins.open', mock_open(read_data='tconst\ttitleType\tprimaryTitle\toriginalTitle\tyear\n'))
    # def test_get_most_popular_genres_with_io_error(self):
    #     # Test for getting most popular genres for a year with an I/O error
    #     input_file = 'movies.tsv'
    #     expected_result = {'error': f'Error reading input file {input_file}.'}, 500
    #     with patch('pandas.read_csv', side_effect=IOError('test error')):
    #         result = get_most_popular_genres('2022', 1)
    #         self.assertEqual(result, expected_result)


    # @patch('data_logic.load_data', side_effect=FileNotFoundError('test error'))
    # def test_get_most_popular_genres_with_missing_input_file(self, load_data_mock):
    #     # Test for getting most popular genres for a year with missing input file
    #     expected_result = {'error': 'Input file movies.tsv not found.'}, 404
    #     result = get_most_popular_genres('2022', 1)
    #     self.assertEqual(result, expected_result)

    @patch('data_logic.load_data', side_effect=IOError('test error'))
    def test_get_most_popular_genres_with_io_error(self, load_data_mock):
        # Test for getting most popular genres for a year with an I/O error
        expected_result = {'error': 'Error reading input file movies.tsv.'}, 500
        result = get_most_popular_genres('2022', 1)
        self.assertEqual(result, expected_result)