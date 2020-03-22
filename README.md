# Convert lat/lon coordinates to Landsat-8 row/path pair(s)

## Build image
```sh
docker build -t landsat8-converter .
```

## Usage
Convert lat/lon coordinates to Landsat-8 row/path pair(s).
```sh
docker run --rm -it -v `pwd`:/workspace landsat8-converter python3 src/latlon_to_rowpath.py --help
```
```sh
usage: latlon_to_rowpath.py [-h] -t LATITUDE -n LONGITUDE -m MODE

optional arguments:
  -h, --help            show this help message and exit
  -t LATITUDE, --latitude LATITUDE
                        Latitude in signed degrees fomat (DDD.dddd)
  -n LONGITUDE, --longitude LONGITUDE
                        Longitude in signed degrees fomat (DDD.dddd)
  -m MODE, --mode MODE  Choose either daytime captures (D) or nighttime
                        captures (A)
```

* Example:
```sh
docker run --rm -it -v `pwd`:/workspace landsat8-converter python3 src/latlon_to_rowpath.py --latitude 75.0 --longitude 75.0 --mode D
```

## Linting
Autopep8
```bash
docker run \
    --rm -it \
    -v `pwd`:/workspace \
    landsat8-converter /bin/bash -c \
        "pip3 install -r requirements-dev.txt && \
        autopep8 -i -a -a -r ."
```

Flake8
```bash
docker run \
    --rm -it \
    -v `pwd`:/workspace \
    landsat8-converter /bin/bash -c \
        "pip3 install -r requirements-dev.txt && \
        flake8 --config=.flake8"
```

## Type checking
```bash
docker run \
    --rm -it \
    -v `pwd`:/workspace \
    landsat8-converter /bin/bash -c \
        "pip3 install -r requirements-dev.txt && \
        mypy --config-file mypy.ini ./src/*.py"
```

## Testing
```bash
docker run \
    --rm -it \
    -v `pwd`:/workspace \
    -e "PYTHONPATH=." \
    landsat8-converter /bin/bash -c \
        "pip3 install -r requirements-dev.txt && pytest tests"
```
