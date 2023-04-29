import requests
import json
class Balances():
    def get_my_eth_balance(my_address, endpoint) -> float:
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getBalance",
            "params": [my_address, "latest"],
            "id": 1
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(endpoint, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            balance_wei = int(response.json()["result"], 16)
            balance_eth = balance_wei / 10 ** 18
            return f'{balance_eth} ETH'
        else:
            raise Exception(
                f"Failed to get ETH balance for {my_address}; status code {response.status_code}")
        
    def get_eth_balance(wallet_address, endpoint) -> float:
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getBalance",
            "params": [wallet_address, "latest"],
            "id": 1
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(endpoint, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            balance_wei = int(response.json()["result"], 16)
            balance_eth = balance_wei / 10 ** 18
            return f'{balance_eth} ETH'
        else:
            raise Exception(
                f"Failed to get ETH balance for {address}; status code {response.status_code}")

    def get_eth_token_balances(wallet_address):
        try:
            url = "https://rpc.ankr.com/multichain/?ankr_getAccountBalance="

            payload = {
                "jsonrpc": "2.0",
                "method": "ankr_getAccountBalance",
                "params": {
                    "blockchain": ["eth"],
                    "walletAddress": wallet_address,
                    "onlyWhitelisted": False
                },
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            assets = response_data['result']['assets']

            token_info = []
            for asset in assets:
                token_name = asset['tokenName']
                token_symbol = asset['tokenSymbol']
                contract_address = asset['contractAddress']
                token_balance = float(asset['balance'])
                usd_balance = float(asset['balanceUsd'])
                token_price_usd = float(asset['tokenPrice'])
                token_info.append({'name': token_name, 'symbol': token_symbol,
                                  'contract_address': contract_address, 'token_balance': token_balance, 'token_price_usd': token_price_usd, 'usd_balance': usd_balance})
            return token_info

        except Exception as e:
            return f"Failed to get ETH token balances: {e}"

    def get_polygon_token_balances(wallet_address):
        try:
            url = "https://rpc.ankr.com/multichain/?ankr_getAccountBalance="

            payload = {
                "jsonrpc": "2.0",
                "method": "ankr_getAccountBalance",
                "params": {
                    "blockchain": ["polygon"],
                    "walletAddress": wallet_address,
                    "onlyWhitelisted": False
                },
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            assets = response_data['result']['assets']

            token_info = []
            for asset in assets:
                token_name = asset['tokenName']
                token_symbol = asset['tokenSymbol']
                contract_address = asset['contractAddress']
                token_balance = float(asset['balance'])
                usd_balance = float(asset['balanceUsd'])
                token_price_usd = float(asset['tokenPrice'])
                token_info.append({'name': token_name, 'symbol': token_symbol,
                                  'contract_address': contract_address, 'token_balance': token_balance, 'token_price_usd': token_price_usd, 'usd_balance': usd_balance})
            return token_info

        except Exception as e:
            return f"Failed to get Polygon token balances: {e}"

    def get_bsc_token_balances(wallet_address):
        try:
            url = "https://rpc.ankr.com/multichain/?ankr_getAccountBalance="

            payload = {
                "jsonrpc": "2.0",
                "method": "ankr_getAccountBalance",
                "params": {
                    "blockchain": ["bsc"],
                    "walletAddress": wallet_address,
                    "onlyWhitelisted": False
                },
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            assets = response_data['result']['assets']

            token_info = []
            for asset in assets:
                token_name = asset['tokenName']
                token_symbol = asset['tokenSymbol']
                contract_address = asset['contractAddress']
                token_balance = float(asset['balance'])
                usd_balance = float(asset['balanceUsd'])
                token_price_usd = float(asset['tokenPrice'])
                token_info.append({'name': token_name, 'symbol': token_symbol,
                                  'contract_address': contract_address, 'token_balance': token_balance, 'token_price_usd': token_price_usd, 'usd_balance': usd_balance})
            return token_info

        except Exception as e:
            return f"Failed to get BSC token balances: {e}"

    def get_fantom_token_balances(wallet_address):
        try:
            url = "https://rpc.ankr.com/multichain/?ankr_getAccountBalance="

            payload = {
                "jsonrpc": "2.0",
                "method": "ankr_getAccountBalance",
                "params": {
                    "blockchain": ["fantom"],
                    "walletAddress": wallet_address,
                    "onlyWhitelisted": False
                },
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            assets = response_data['result']['assets']

            token_info = []
            for asset in assets:
                token_name = asset['tokenName']
                token_symbol = asset['tokenSymbol']
                contract_address = asset['contractAddress']
                token_balance = float(asset['balance'])
                usd_balance = float(asset['balanceUsd'])
                token_price_usd = float(asset['tokenPrice'])
                token_info.append({'name': token_name, 'symbol': token_symbol,
                                  'contract_address': contract_address, 'token_balance': token_balance, 'token_price_usd': token_price_usd, 'usd_balance': usd_balance})
            return token_info

        except Exception as e:
            return f"Failed to get Fantom token balances: {e}"

    def get_avalanche_token_balances(wallet_address):
        try:
            url = "https://rpc.ankr.com/multichain/?ankr_getAccountBalance="

            payload = {
                "jsonrpc": "2.0",
                "method": "ankr_getAccountBalance",
                "params": {
                    "blockchain": ["avalanche"],
                    "walletAddress": wallet_address,
                    "onlyWhitelisted": False
                },
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            assets = response_data['result']['assets']

            token_info = []
            for asset in assets:
                token_name = asset['tokenName']
                token_symbol = asset['tokenSymbol']
                contract_address = asset['contractAddress']
                token_balance = float(asset['balance'])
                usd_balance = float(asset['balanceUsd'])
                token_price_usd = float(asset['tokenPrice'])
                token_info.append({'name': token_name, 'symbol': token_symbol,
                                  'contract_address': contract_address, 'token_balance': token_balance, 'token_price_usd': token_price_usd, 'usd_balance': usd_balance})
            return token_info

        except Exception as e:
            return f"Failed to get Avalanche token balances: {e}"

    def get_arbitrum_token_balances(wallet_address):
        try:
            url = "https://rpc.ankr.com/multichain/?ankr_getAccountBalance="

            payload = {
                "jsonrpc": "2.0",
                "method": "ankr_getAccountBalance",
                "params": {
                    "blockchain": ["arbitrum"],
                    "walletAddress": wallet_address,
                    "onlyWhitelisted": False
                },
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            assets = response_data['result']['assets']

            token_info = []
            for asset in assets:
                token_name = asset['tokenName']
                token_symbol = asset['tokenSymbol']
                contract_address = asset['contractAddress']
                token_balance = float(asset['balance'])
                usd_balance = float(asset['balanceUsd'])
                token_price_usd = float(asset['tokenPrice'])
                token_info.append({'name': token_name, 'symbol': token_symbol,
                                  'contract_address': contract_address, 'token_balance': token_balance, 'token_price_usd': token_price_usd, 'usd_balance': usd_balance})
            return token_info

        except Exception as e:
            return f"Failed to get Arbitrum token balances: {e}"

    def get_syscoin_token_balances(wallet_address):
        try:
            url = "https://rpc.ankr.com/multichain/?ankr_getAccountBalance="

            payload = {
                "jsonrpc": "2.0",
                "method": "ankr_getAccountBalance",
                "params": {
                    "blockchain": ["syscoin"],
                    "walletAddress": wallet_address,
                    "onlyWhitelisted": False
                },
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            assets = response_data['result']['assets']

            token_info = []
            for asset in assets:
                token_name = asset['tokenName']
                token_symbol = asset['tokenSymbol']
                contract_address = asset['contractAddress']
                token_balance = float(asset['balance'])
                usd_balance = float(asset['balanceUsd'])
                token_price_usd = float(asset['tokenPrice'])
                token_info.append({'name': token_name, 'symbol': token_symbol,
                                  'contract_address': contract_address, 'token_balance': token_balance, 'token_price_usd': token_price_usd, 'usd_balance': usd_balance})
            return token_info

        except Exception as e:
            return f"Failed to get Syscoin token balances: {e}"

    def get_optimism_token_balances(wallet_address):
        try:
            url = "https://rpc.ankr.com/multichain/?ankr_getAccountBalance="

            payload = {
                "jsonrpc": "2.0",
                "method": "ankr_getAccountBalance",
                "params": {
                    "blockchain": ["optimism"],
                    "walletAddress": wallet_address,
                    "onlyWhitelisted": False
                },
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            assets = response_data['result']['assets']

            token_info = []
            for asset in assets:
                token_name = asset['tokenName']
                token_symbol = asset['tokenSymbol']
                contract_address = asset['contractAddress']
                token_balance = float(asset['balance'])
                usd_balance = float(asset['balanceUsd'])
                token_price_usd = float(asset['tokenPrice'])
                token_info.append({'name': token_name, 'symbol': token_symbol,
                                  'contract_address': contract_address, 'token_balance': token_balance, 'token_price_usd': token_price_usd, 'usd_balance': usd_balance})
            return token_info

        except Exception as e:
            return f"Failed to get Optimism token balances: {e}"