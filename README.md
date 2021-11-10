# F1 API

An experimental web service which provides a historical record of motor racing
data for non-commercial purposes.

The API provides data for the [Formula One][1] series, from the beginning of
the world championship in 1950.


## Acknowledgement

The dataset is provided by [Ergast Developer][2]


## Quickstart Guide

1. Install dependencies with [poetry][3]

`poetry install`

2. Run a development server

`poetry run flask run`

3. Navigate to http://127.0.0.1:5000/api


## Data Routes

Every CSV file in `data/` represents a route.

The data routes are in `api/v1/resource/<route>` format.

For example, all drivers can be found in http://127.0.0.1:5000/api/v1/resources/drivers/all.

Queries can be performed by specifying the column and value.

For example, driver number 33 is in http://127.0.0.1:5000/api/v1/resources/drivers?number=33.


[1]: https://en.wikipedia.org/wiki/Formula_One/
[2]: http://ergast.com/mrd/
[3]: https://python-poetry.org/docs/
