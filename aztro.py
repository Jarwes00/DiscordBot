import requests
from pyaztro.helpers import parse_date, parse_date_range, parse_time, signs, days
import pyaztro.exceptions


class Aztro(object): # NOQA
    def __init__(self, sign, day='today', timezone=None):
        base_url = 'https://aztro.sameerkumar.website'
        sign = str(sign).lower() if sign else sign
        day = str(day).lower() if day else day
        self.sign = sign
        self.day = day
        if sign not in signs:
            raise pyaztro.exceptions.PyAztroSignException('Invalid sign {0} passed'.format(sign), sign)
        if day not in days:
            raise pyaztro.exceptions.PyAztroDayException('Invalid day {0} passed'.format(day), day)
        params = (
            ('sign', sign),
            ('day', day),
            ('timezone', timezone)

        )
        try:
            r = requests.post(url=base_url, params=params)
            if r.status_code == 200:
                data = r.json()
            else:
                raise pyaztro.exceptions.PyAztroInvalidAPIResponseException(
                    'Could not get a successful response from aztro API', r.content) # NOQA
        except requests.exceptions.RequestException as re:
            raise pyaztro.exceptions.PyAztroRequestsException('Exception during making request to aztro API', re) # NOQA

        try:
            self.lucky_time = parse_time(data['lucky_time'])
            self.description = data['description']
            self.date_range = parse_date_range(data['date_range'])
            self.color = data['color']
            self.mood = data['mood']
            self.compatibility = data['compatibility']
            self.current_date = parse_date(data['current_date'])
            self.lucky_number = int(data['lucky_number'])
        except Exception as err:
            raise pyaztro.exceptions.PyAztroInvalidAPIResponseException('Could not parse data from aztro API', err) # NOQA

    # todo: def get_full_message(self, string) < Zebrać dane i przekazać. # NOQA
