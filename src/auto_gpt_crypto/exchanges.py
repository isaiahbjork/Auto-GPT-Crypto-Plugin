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
            for item in values_list:  # iterate through the values in the list
                # convert exchange name to lowercase after removing any leading or trailing whitespace
                exchange_name = item.strip().lower()
                if exchange_name not in ccxt_exchanges:  # check if the exchange is not available in ccxt
                    # append the exchange to the not available exchanges list
                    not_available_exchanges.append(exchange_name)
            if not_available_exchanges:  # check if there are any exchanges that are not available in ccxt
                # return the list of exchanges that are not available in ccxt
                return f'Please review the exchanges.txt and add the correct exchanges to the .env: {not_available_exchanges}'
            else:
                return ccxt_exchanges  # return the list of all exchanges available in ccxt
        except Exception as e:
            return f"An error occurred while retrieving available exchanges: {str(e)}"

    def balance_on_kraken(kraken_api, kraken_secret):
        try:
            kraken = ccxt.kraken({
                'apiKey': kraken_api,
                'secret': kraken_secret,
            })
            balances = kraken.fetch_balance()

            non_zero_balances = []

            for currency, balance in balances['total'].items():
                if balance != 0:
                    non_zero_balances.append({'currency': currency, 'balance': balance})

            return non_zero_balances
        except Exception as e:
            return f"An error occurred while retrieving balance from Kraken: {str(e)}"

    def balance_on_coinbase(coinbase_api, coinbase_secret):
        try:
            coinbase = ccxt.coinbase({
                'apiKey': coinbase_api,
                'secret': coinbase_secret,
            })
            balances = coinbase.fetch_balance()

            non_zero_balances = []

            for currency, balance in balances['total'].items():
                if balance != 0:
                    non_zero_balances.append({'currency': currency, 'balance': balance})

            return non_zero_balances

        except Exception as e:
            return f"An error occurred while retrieving balance from Coinbase: {str(e)}"
