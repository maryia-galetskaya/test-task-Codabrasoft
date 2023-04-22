import unittest
from unittest.mock import patch, mock_open
from business_logic import get_most_popular_genres
from data_logic import check_input_file, load_data
from datetime import datetime
import pandas as pd
import os


class TestBusinessLogic(unittest.TestCase):

    # @patch('builtins.open', mock_open(read_data='tconst\ttitleType\tprimaryTitle\toriginalTitle\tyear\n'))
    # def test_get_most_popular_genres_with_valid_year(self):
    #     # Test for getting most popular genres for a valid year
    #     expected_result = [{"count": 5727,"genres": "Drama"}]
    #     result = get_most_popular_genres('2022', 1)
    #     self.assertEqual(result, expected_result)

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
        self.assertEqual(result, expected_result)

    def test_get_most_popular_genres_with_no_genres(self):
        # Test for getting most popular genres for a year with no available genres
        input_file = 'movies.tsv'
        expected_result = {'error': f'No data found for year 1886.'}, 404
        result = get_most_popular_genres(1886, 10)
        self.assertEqual(result, expected_result)
    
    # # @patch('pandas.read_csv', return_value=pd.DataFrame())
    # # def test_load_data_with_empty_input_file(self, mock_read_csv):
    # #     # Test for loading data from an empty input file
    # #     input_file = 'movies.tsv'
    # #     expected_result = {'error': f'Input file {input_file} is empty or contains no data.'}, 500
    # #     result = load_data()
    # #     self.assertEqual(result, expected_result)

    # # @patch('pandas.read_csv', return_value=pd.DataFrame)
    # # def test_load_data_with_empty_input_file(self, mock_read_csv):
    # #     # Test for loading data from an empty input file
    # #     expected_result = {'error': 'Input file movies.tsv is empty or contains no data.'}, 500
    # #     result = load_data()
    # #     self.assertEqual(result, expected_result)



class TestLoadData(unittest.TestCase):

    @patch('builtins.open', side_effect=FileNotFoundError('test error'))
    def test_get_most_popular_genres_with_missing_input_file(self, mock_open):
        # Test for getting most popular genres for a year with missing input file
        input_file = 'movies.tsv'
        expected_result = {'error': f'Input file {input_file} not found.'}, 404
        result = get_most_popular_genres('2022', 1)
        self.assertEqual(result, expected_result)

    @patch('builtins.open', mock_open(read_data='tconst\ttitleType\tprimaryTitle\toriginalTitle\tyear\n'))
    def test_get_most_popular_genres_with_io_error(self):
        # Test for getting most popular genres for a year with an I/O error
        input_file = 'movies.tsv'
        expected_result = {'error': f'Error reading input file {input_file}.'}, 500
        with patch('pandas.read_csv', side_effect=IOError('test error')):
            result = get_most_popular_genres('2022', 1)
            self.assertEqual(result, expected_result)


#     def test_check_input_file(self):
#         # test if input file exists
#         self.assertTrue(os.path.exists('movies.tsv'))
        
#         # test if FileNotFoundError is raised when input file doesn't exist
#         with self.assertRaises(FileNotFoundError):
#             check_input_file(input_file='non_existent_file.tsv')
            
#     def test_load_data(self):
#         # test if function returns a pandas dataframe with the expected column
#         data = load_data()
#         self.assertIsInstance(data, pd.DataFrame)
#         self.assertIn('startYear', data.columns.tolist())
        
#         # # test if function raises an error when input file is not found
#         # with self.assertRaises(FileNotFoundError):
#         #     load_data('non_existent_file.tsv')
            
#         # test if function returns an error dictionary when input file is empty
#         with open('empty_file.tsv', 'w') as f:
#             f.write('')
#         with self.assertRaises(pd.errors.EmptyDataError):
#             load_data()
#         os.remove('empty_file.tsv')
        
#         # test if function returns an error dictionary when an unexpected error occurs
#         with open('corrupted_file.tsv', 'w') as f:
#             f.write('col1\tcol2\n1\t2\ninvalid_line\n')
#         with self.assertRaises(Exception):
#             load_data()
#         os.remove('corrupted_file.tsv')
