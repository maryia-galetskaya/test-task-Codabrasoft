import os
import pandas as pd


def check_input_file():
    input_file = 'movies.tsv'
    if not os.path.exists(input_file):
        print('exception')
        raise FileNotFoundError(f"Input file {input_file} not found.")
        # return {'error': f'Input file {input_file} not found.'}, 404
    return 'movies.tsv'
    


def load_data():
    check_input_file()
    input_file = 'movies.tsv'
    try:
        data = pd.read_csv(input_file, sep='\t', header=0)
    except:
        return {'error': f'Error reading input file {input_file}.'}, 500
    
#     return data

    # return pd.read_csv('movies.tsv', sep='\t', header=0)
