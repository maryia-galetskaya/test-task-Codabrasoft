# Most Popular Genres API

This is a Flask-based REST API that provides the most popular movie genres for a given year.

## Requirements

The following dependencies are required to run the application:

- Flask==2.1.0
- pandas==1.3.4
- os
- datetime

## Installation

To install the dependencies, run the following command:

```bash
pip install -r requirements.txt
```


## Usage

To start the API, run the following command:

```bash
python app.py
```

By default, the API will be available at http://127.0.0.1:5000.

To retrieve the most popular genres for a given year, make a GET request to the '/api/most_popular_genres' endpoint with the year parameter set to the desired year: http://127.0.0.1:5000/api/most_popular_genres?year=2010




Optionally, you can also provide the row_count parameter to limit the number of results returned:

http://127.0.0.1:5000/api/most_popular_genres?year=2010&row_count=5



## Docker
This application can also be run as a Docker container. To do so, follow these steps:
1. Build the Docker image:  

    ```bash 
    docker build -t my-app .
    ```
2. Run the Docker container:
    ```bash 
    docker run -p 5000:5000 my-app
    ```

By default, the API will be available at http://127.0.0.1:5000. You can access it using the same endpoints as described in the previous section.

## Testing
To run the unit tests, run the following command:
```bash 
python unit_tests.py
```

To run the integration tests, run the following command:
```bash 
python integration_tests.py
```