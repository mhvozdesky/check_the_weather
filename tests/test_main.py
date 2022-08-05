import unittest
import weather_service
from unittest.mock import patch, MagicMock
import os
import io
from coordinates import get_coordinates
from weather_service import (get_weather,
                             _get_openweather_response,
                             _parse_openweather_response,
                             openweather_url_pat)
from exceptions import ApiServiceError, ParseError


class TestMain(unittest.TestCase):
    def test_get_coordinates(self):
        os.environ["LATITUDE"] = "40.1"
        os.environ["LONGITUDE"] = "30.1"

        coordinates = get_coordinates()

        self.assertEqual(coordinates.latitude, '40.1')
        self.assertEqual(coordinates.longitude, '30.1')

    # @patch("http.client.HTTPSConnection")
    # @patch("http.client.HTTPResponse")
    # def test_get_openweather_response(self, mock_res, mock_conn):
    #     mock_res.status = 200
    #     mock_conn.getresponse = MagicMock(return_value=mock_res)
    #
    #     a = _get_openweather_response(40.1, 30.2, 'sewww')
    #     print

    @patch('weather_service.urllib.request.urlopen')
    def test_get_openweather_response(self, mock_res):
        mock_res.return_value = io.StringIO()
        lat = 40.1
        long = 30.2
        appid = 'sefs12sefses'
        _get_openweather_response(lat, long, appid)
        self.assertEqual(mock_res.call_count, 1)
        self.assertEqual(mock_res.call_args[0][0],
                         openweather_url_pat.format(latitude=lat,
                                                    longitude=long,
                                                    appid=appid))

    @patch.object(weather_service,
                  'openweather_url_pat',
                  'https://spam{latitude}{longitude}{appid}')
    def test_get_openweather_response_error(self):
        lat = 40.1
        long = 30.2
        appid = 'sefs12sefses'
        with self.assertRaises(ApiServiceError) as context:
            _get_openweather_response(lat, long, appid)

        self.assertEqual('could not get a response from the server',
                         context.exception.args[0])


if __name__ == '__main__':
    unittest.main()
