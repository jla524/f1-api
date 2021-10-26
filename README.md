# F1 API

An API for Formula 1 data.


# Acknowledgement

The dataset is provided by [Ergast Developer](http://ergast.com/mrd/)


# Instructions to run
```
mkdir data

wget http://ergast.com/downloads/f1db_csv.zip

unzip -d data f1db_csv.zip

poetry install

poetry run ./run.sh
```

# TODOs
- Add unit tests

- Make pandas filter case insensitive
