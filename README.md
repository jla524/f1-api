# F1 API

A simple API made for Formula 1 data.


# Acknowledgement

The dataset is provided by [Ergast Developer](http://ergast.com/mrd/)


# Download the dataset
```
mkdir data/

wget http://ergast.com/downloads/f1db_csv.zip

unzip -d data f1db_csv.zip

rm f1db_csv.zip
```


# Instructions to run
```
poetry install

poetry run flask run
```


# TODOs

- Add all files in the dataset to route

- Simplify process to download dataset
