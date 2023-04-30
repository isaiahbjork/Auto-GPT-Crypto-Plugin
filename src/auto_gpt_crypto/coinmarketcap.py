import requests

class CoinMarketCap():
    def get_upcoming_airdrops(cmc_api):
        url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/airdrops'
        params = {
            'status': 'UPCOMING',
            'CMC_PRO_API_KEY': cmc_api
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception if the response status is not OK (2xx)

            json_data = response.json()
            return json_data

        except requests.exceptions.RequestException as e:
            return f'Error fetching data from CMC API: {e}'
        
    def convert_crypto(cmc_api, amount, symbol, conversion_symbol):
        url = f'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'
        params = {
            'amount': float(amount),
            'symbol': symbol,
            'convert': conversion_symbol,
            'CMC_PRO_API_KEY': cmc_api
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception if the response status is not OK (2xx)

            json_data = response.json()
            return json_data

        except requests.exceptions.RequestException as e:
            return f'Error fetching data from CMC API: {e}'