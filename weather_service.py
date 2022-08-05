import os
import urllib.request
import json
import ssl
from urllib.error import URLError
from json.decoder import JSONDecodeError
from coordinates import Coordinates
from typing import NamedTuple
from datetime import datetime
from coordinates import CITY
from exceptions import ApiServiceError, ParseError

Celsius = int
openweather_url_pat = 'https://api.openweathermap.org/data/2.5/forecast?lat={latitude}' \
                      '&lon={longitude}&appid={appid}&units' \
                      '=metric&lang=ua'


def _get_openweather_response(latitude: float, longitude: float, appid: str) -> str:
    ctx = ssl.create_default_context()
    url = openweather_url_pat.format(latitude=latitude,
                                     longitude=longitude,
                                     appid=appid)

    try:
        return urllib.request.urlopen(url, context=ctx).read()
    except URLError:
        raise ApiServiceError('could not get a response from the server')


def _parse_openweather_response(openweather_response) -> dict:
    try:
        openweather_dict = json.loads(openweather_response)
    except JSONDecodeError:
        raise ParseError('unable to read json')

    return openweather_dict


def get_weather(coordinates: Coordinates) -> dict:
    latitude = coordinates.latitude
    longitude = coordinates.longitude
    appid = os.environ.get('API_KEY')
    openweather_response = _get_openweather_response(latitude, longitude, appid)
    weather = _parse_openweather_response(openweather_response)
    return weather


if __name__ == '__main__':
    get_weather(Coordinates(latitude=os.environ.get('LATITUDE'),
                            longitude=os.environ.get('LONGITUDE')))
