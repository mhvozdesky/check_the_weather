import os
from collections import namedtuple

Coordinates = namedtuple('Coordinates', ['latitude', 'longitude'])
CITY = os.environ.get('CITY')


def get_coordinates() -> Coordinates:
    return Coordinates(latitude=os.environ.get('LATITUDE'),
                       longitude=os.environ.get('LONGITUDE'))
