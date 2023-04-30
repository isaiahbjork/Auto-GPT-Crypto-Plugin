import requests

class Fcs():
    def get_crypto_pivot_points(fcs_api, symbol, timeframe):
        url = f'https://fcsapi.com/api-v3/crypto/pivot_points'
        params = {
            'symbol': symbol,
            'period': timeframe,
            'access_key': fcs_api
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception if the response status is not OK (2xx)

            json_data = response.json()
            return json_data

        except requests.exceptions.RequestException as e:
            return f'Error fetching data from FCS API: {e}'
        
    def get_crypto_moving_averages(fcs_api, symbol, timeframe):
        url = f'https://fcsapi.com/api-v3/crypto/ma_avg'
        params = {
            'symbol': symbol,
            'period': timeframe,
            'access_key': fcs_api
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception if the response status is not OK (2xx)

            json_data = response.json()
            return json_data

        except requests.exceptions.RequestException as e:
            return f'Error fetching data from FCS API: {e}'
        
    def get_crypto_technical_indicators(fcs_api, symbol, timeframe):
        url = f'https://fcsapi.com/api-v3/crypto/indicators'
        params = {
            'symbol': symbol,
            'period': timeframe,
            'access_key': fcs_api
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception if the response status is not OK (2xx)

            json_data = response.json()
            return json_data

        except requests.exceptions.RequestException as e:
            return f'Error fetching data from FCS API: {e}'

