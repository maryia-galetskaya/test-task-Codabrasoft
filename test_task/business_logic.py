from datetime import datetime
from data_logic import load_data

class CustomException(Exception):
    pass

def get_most_popular_genres(year, row_count):
    try:
        year = int(year)
    except ValueError:
        return {'error': 'Year parameter must be an integer'}, 400
    
    current_year = datetime.now().year
    # Movies were not commercially screened until December 28, 1895, so I set a lower bound of 1885 for the year parameter.
    if year < 1885 or year > current_year:
        return {'error': f'Year parameter must be between 1885 and {current_year}.'}, 400
    
    try:
        data = load_data()
    except CustomException as e:
        return {'error': str(e)}, 500
    
    if isinstance(data, tuple):
        return data


    year_data = data[(data['genres'] != '\\N') & (data['startYear'] == year)]


    if year_data.empty:
        return {'error': f'No data found for year {year}.'}, 404


    genres = year_data['genres'].str.split(',').explode().value_counts().reset_index()
    genres = genres.sort_values('count', ascending=False)
    genres = genres.head(row_count)

    return genres.to_dict(orient='records'), 200
