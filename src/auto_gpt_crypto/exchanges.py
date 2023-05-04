import os
import ccxt


class Exchanges():
    def available_crypto_exchanges():
        try:
            # retrieve environment variable containing comma-separated values
            exchanges = os.environ.get("EXCHANGES")
            if not exchanges:  # check if exchanges is empty or not set
                return "Set EXCHANGES in the .env file"
            # split the values using the comma delimiter and store them in a list
            values_list = exchanges.split(",")
            # get a list of all exchanges available in ccxt library
            ccxt_exchanges = [exchange.lower() for exchange in ccxt.exchanges]
            # create an empty list to store the exchanges that are not available in ccxt
            not_available_exchanges = []
            available_exchanges = []
            for item in values_list:  # iterate through the values in the list
                # convert exchange name to lowercase after removing any leading or trailing whitespace
                exchange_name = item.strip().lower()
                if exchange_name not in ccxt_exchanges:  # check if the exchange is not available in ccxt
                    # append the exchange to the not available exchanges list
                    not_available_exchanges.append(exchange_name)
                else: 
                    available_exchanges.append(exchange_name)
            if not_available_exchanges:  # check if there are any exchanges that are not available in ccxt
                # return the list of exchanges that are not available in ccxt
                return f'Please review the .env and add the correct exchanges: {not_available_exchanges}'
            else:
                return available_exchanges  # return the list of all exchanges available in ccxt
        except Exception as e:
            return f"An error occurred while retrieving available exchanges: {str(e)}"

    def balance_on_exchange(exchange):
        try:
            exchange_class = getattr(ccxt, exchange)
            cap_ex = exchange.upper()
            api_key = os.getenv(f'{cap_ex}_API_KEY')
            api_secret = os.getenv(f'{cap_ex}_SECRET')
            if api_key is None or api_secret is None:
                raise ValueError(f"No API key or secret found for {exchange} exchange. Please set in .env")
            exchange = exchange_class({
                'apiKey': api_key,
                'secret': api_secret,
            })
            balances = exchange.fetch_balance()

            non_zero_balances = []

            for currency, balance in balances['total'].items():
                if balance != 0:
                    non_zero_balances.append({'currency': currency, 'balance': balance})

            return non_zero_balances

        except Exception as e:
            return f"An error occurred while retrieving balance from {exchange}: {str(e)}"

    def place_market_order_on_coinbase(coinbase_api, coinbase_secret, symbol, side, amount):
        exchange = ccxt.coinbase({
            'apiKey': coinbase_api,
            'secret': coinbase_secret,
        })

        order = exchange.create_order(symbol, 'market', side, amount)

        return order

    def fetch_crypto_candlesticks(exchange, symbol, side, amount):
        exchange_class = getattr(ccxt, exchange)
        cap_ex = exchange.upper()
        api_key = os.getenv(f'{cap_ex}_API_KEY')
        api_secret = os.getenv(f'{cap_ex}_API_SECRET')
        exchange = exchange_class({
            'apiKey': api_key,
            'secret': api_secret,
        })

        order = exchange.create_order(symbol, 'market', side, amount)

        return order
