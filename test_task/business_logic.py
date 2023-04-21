import os
import pandas as pd
from datetime import datetime
from data_logic import  check_input_file, load_data


def get_most_popular_genres(year, row_count):
    try:
        year = int(year)
    except ValueError:
        return {'error': 'Year parameter must be an integer'}, 400
    
    current_year = datetime.now().year
    # Movies were not commercially screened until December 28, 1895, so I set a lower bound of 1885 for the year parameter.
    if year < 1885 or year > current_year:
        return {'error': f'Year parameter must be between 1885 and {current_year}.'}, 400
       

    # input_file = 'movies.tsv'
    # if not os.path.exists(input_file):
    #     return {'error': f'Input file {input_file} not found.'}, 404\
    input_file = check_input_file()
    # data = load_data()

    try:
        data = pd.read_csv(input_file, sep='\t', header=0)
    except:
        return {'error': f'Error reading input file {input_file}.'}, 500

    year_data = data[data['startYear'] == year]

    if year_data.empty:
        return {'error': f'No data found for year {year}.'}, 404

    genres = year_data['genres'].str.split(',').explode().value_counts().reset_index()
    genres = genres.sort_values('count', ascending=False)
    genres = genres.head(row_count)

    return genres.to_dict(orient='records'), 200
