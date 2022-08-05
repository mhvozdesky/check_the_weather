import os
from datetime import datetime


def format_weather(weather: dict) -> str:
    weather_text = ''
    weather_text += f'Weather in {os.environ.get("CITY")}\n'

    weather_list = weather['list']

    for weather_item in weather_list:
        date_utc = datetime.fromtimestamp(int(weather_item['dt']))
        date = datetime.strftime(date_utc, '%d.%m.%Y %H:%M')
        weather_item_main = weather_item['main']

        weather_text += date + '\n'
        weather_text += f'  temp: {weather_item_main["temp"]}, feels_like: ' \
                        f'{weather_item_main["feels_like"]}, temp_min: ' \
                        f'{weather_item_main["temp_min"]}, temp_max: ' \
                        f'{weather_item_main["temp_max"]}' + '\n'

        weather_text += '  weather: '
        for index, i in enumerate(weather_item['weather']):
            sep = '' if index == 0 else ', '
            weather_text += sep + i['description']

        weather_text += '\n'
        weather_text += f'  clouds: {weather_item["clouds"]["all"]}' + '\n'

        weather_text += f'  wind: {weather_item["wind"]["speed"]}'

        weather_text += '\n\n'

    return weather_text
