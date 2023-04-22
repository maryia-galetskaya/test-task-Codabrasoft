import os
import pandas as pd


def check_input_file(input_file='movies.tsv'):
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} not found.")
    return input_file


def load_data():
    input_file = check_input_file()
    try:
        data = pd.read_csv(input_file, sep='\t', header=0)
        return data
    except FileNotFoundError:
        return {'error': f'Input file {input_file} not found.'}, 404
    except pd.errors.EmptyDataError:
        return {'error': f'Input file {input_file} is empty or contains no data.'}, 500
    except:
        return {'error': f'Error reading input file {input_file}.'}, 500