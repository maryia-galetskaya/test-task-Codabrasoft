from flask import Flask, jsonify, request
from business_logic import get_most_popular_genres


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/api/most_popular_genres', methods=['GET'])
def get_genres():
    year = request.args.get('year')
    row_count = request.args.get('row_count', default=5, type=int)

    if not year:
        return jsonify(error='Year parameter is missing'), 400

    genres, status_code = get_most_popular_genres(year, row_count)

    if 'error' in genres:
        return jsonify(error=genres['error']), status_code

    return jsonify(genres)


if __name__ == '__main__':
    app.run(debug=True)
