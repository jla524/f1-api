# F1 API

A simple API made for Formula 1 data.


# Acknowledgement

The dataset is provided by [Ergast Developer](http://ergast.com/mrd/)


# Instructions to run
```
wget http://ergast.com/downloads/f1db_csv.zip

unzip -d data f1db_csv.zip && rm f1db_csv.zip

poetry install

poetry run flask run
```


# TODOs

- Add all F1 data files to route

- Improve code reuse for unit tests
