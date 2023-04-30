import requests

class Transactions():
    def get_eth_transaction_data(transaction_hash):
        try:
            url = "https://rpc.ankr.com/eth"

            payload = {
                "jsonrpc": "2.0",
                "method": "eth_getTransactionByHash",
                "params": [transaction_hash],
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            data = response_data
            transaction_data = response_data['result']

            block_hash = transaction_data['blockHash']
            # Convert from hex to decimal
            block_number = int(transaction_data['blockNumber'], 16)
            from_address = transaction_data['from']
            to_address = transaction_data['to']
            transaction_hash = transaction_data['hash']
            value_wei = int(transaction_data['value'], 16)  # Convert from hex to decimal

            value_ether = value_wei / (10 ** 18)
            tx = {
                "block_hash": block_hash,
                "block_number": block_number,
                "from_address": from_address,
                "to_address": to_address,
                "transaction_hash": transaction_hash,
                "value_ether": value_ether

            }
            return tx

        except Exception as e:
            return f"Failed to get ETH Transaction Data: {e}"
    
    def get_polygon_transaction_data(transaction_hash):
        try:
            url = "https://rpc.ankr.com/polygon"

            payload = {
                "jsonrpc": "2.0",
                "method": "eth_getTransactionByHash",
                "params": [transaction_hash],
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            data = response_data
            transaction_data = response_data['result']

            block_hash = transaction_data['blockHash']
            # Convert from hex to decimal
            block_number = int(transaction_data['blockNumber'], 16)
            from_address = transaction_data['from']
            to_address = transaction_data['to']
            transaction_hash = transaction_data['hash']
            value_wei = int(transaction_data['value'], 16)  # Convert from hex to decimal

            value_matic = value_wei / (10 ** 18)
            tx = {
                "block_hash": block_hash,
                "block_number": block_number,
                "from_address": from_address,
                "to_address": to_address,
                "transaction_hash": transaction_hash,
                "value_matic": value_matic

            }
            return tx

        except Exception as e:
            return f"Failed to get Polygon Transaction Data: {e}"

    def get_bsc_transaction_data(transaction_hash):
        try:
            url = "https://rpc.ankr.com/bsc"

            payload = {
                "jsonrpc": "2.0",
                "method": "eth_getTransactionByHash",
                "params": [transaction_hash],
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            data = response_data
            transaction_data = response_data['result']

            block_hash = transaction_data['blockHash']
            # Convert from hex to decimal
            block_number = int(transaction_data['blockNumber'], 16)
            from_address = transaction_data['from']
            to_address = transaction_data['to']
            transaction_hash = transaction_data['hash']
            value_wei = int(transaction_data['value'], 16)  # Convert from hex to decimal

            value_bsc = value_wei / (10 ** 18)
            tx = {
                "block_hash": block_hash,
                "block_number": block_number,
                "from_address": from_address,
                "to_address": to_address,
                "transaction_hash": transaction_hash,
                "value_bsc": value_bsc

            }
            return tx

        except Exception as e:
            return f"Failed to get BSC Transaction Data: {e}"
    
    def get_fantom_transaction_data(transaction_hash):
        try:
            url = "https://rpc.ankr.com/fantom"

            payload = {
                "jsonrpc": "2.0",
                "method": "eth_getTransactionByHash",
                "params": [transaction_hash],
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            data = response_data
            transaction_data = response_data['result']

            block_hash = transaction_data['blockHash']
            # Convert from hex to decimal
            block_number = int(transaction_data['blockNumber'], 16)
            from_address = transaction_data['from']
            to_address = transaction_data['to']
            transaction_hash = transaction_data['hash']
            value_wei = int(transaction_data['value'], 16)  # Convert from hex to decimal

            value_fantom = value_wei / (10 ** 18)
            tx = {
                "block_hash": block_hash,
                "block_number": block_number,
                "from_address": from_address,
                "to_address": to_address,
                "transaction_hash": transaction_hash,
                "value_fantom": value_fantom

            }
            return tx

        except Exception as e:
            return f"Failed to get Fantom Transaction Data: {e}"

    
    def get_arbitrum_transaction_data(transaction_hash):
        try:
            url = "https://rpc.ankr.com/arbitrum"

            payload = {
                "jsonrpc": "2.0",
                "method": "eth_getTransactionByHash",
                "params": [transaction_hash],
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            data = response_data
            transaction_data = response_data['result']

            block_hash = transaction_data['blockHash']
            # Convert from hex to decimal
            block_number = int(transaction_data['blockNumber'], 16)
            from_address = transaction_data['from']
            to_address = transaction_data['to']
            transaction_hash = transaction_data['hash']
            value_wei = int(transaction_data['value'], 16)  # Convert from hex to decimal

            value_arbitrum = value_wei / (10 ** 18)
            tx = {
                "block_hash": block_hash,
                "block_number": block_number,
                "from_address": from_address,
                "to_address": to_address,
                "transaction_hash": transaction_hash,
                "value_arbitrum": value_arbitrum

            }
            return tx

        except Exception as e:
            return f"Failed to get Arbitrum Transaction Data: {e}"
    
    def get_avalanche_transaction_data(transaction_hash):
        try:
            url = "https://rpc.ankr.com/avalanche"

            payload = {
                "jsonrpc": "2.0",
                "method": "eth_getTransactionByHash",
                "params": [transaction_hash],
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            data = response_data
            transaction_data = response_data['result']

            block_hash = transaction_data['blockHash']
            # Convert from hex to decimal
            block_number = int(transaction_data['blockNumber'], 16)
            from_address = transaction_data['from']
            to_address = transaction_data['to']
            transaction_hash = transaction_data['hash']
            value_wei = int(transaction_data['value'], 16)  # Convert from hex to decimal

            value_avalanche = value_wei / (10 ** 18)
            tx = {
                "block_hash": block_hash,
                "block_number": block_number,
                "from_address": from_address,
                "to_address": to_address,
                "transaction_hash": transaction_hash,
                "value_avalanche": value_avalanche

            }
            return tx

        except Exception as e:
            return f"Failed to get Avalanche Transaction Data: {e}"
    
    def get_optimism_transaction_data(transaction_hash):
        try:
            url = "https://rpc.ankr.com/optimism"

            payload = {
                "jsonrpc": "2.0",
                "method": "eth_getTransactionByHash",
                "params": [transaction_hash],
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            data = response_data
            transaction_data = response_data['result']

            block_hash = transaction_data['blockHash']
            # Convert from hex to decimal
            block_number = int(transaction_data['blockNumber'], 16)
            from_address = transaction_data['from']
            to_address = transaction_data['to']
            transaction_hash = transaction_data['hash']
            value_wei = int(transaction_data['value'], 16)  # Convert from hex to decimal

            value_optimism = value_wei / (10 ** 18)
            tx = {
                "block_hash": block_hash,
                "block_number": block_number,
                "from_address": from_address,
                "to_address": to_address,
                "transaction_hash": transaction_hash,
                "value_optimism": value_optimism

            }
            return tx

        except Exception as e:
            return f"Failed to get Optimism Transaction Data: {e}"
        
    def get_syscoin_transaction_data(transaction_hash):
        try:
            url = "https://rpc.ankr.com/syscoin"

            payload = {
                "jsonrpc": "2.0",
                "method": "eth_getTransactionByHash",
                "params": [transaction_hash],
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            data = response_data
            transaction_data = response_data['result']

            block_hash = transaction_data['blockHash']
            # Convert from hex to decimal
            block_number = int(transaction_data['blockNumber'], 16)
            from_address = transaction_data['from']
            to_address = transaction_data['to']
            transaction_hash = transaction_data['hash']
            value_wei = int(transaction_data['value'], 16)  # Convert from hex to decimal

            value_syscoin = value_wei / (10 ** 18)
            tx = {
                "block_hash": block_hash,
                "block_number": block_number,
                "from_address": from_address,
                "to_address": to_address,
                "transaction_hash": transaction_hash,
                "value_syscoin": value_syscoin

            }
            return tx

        except Exception as e:
            return f"Failed to get Syscoin Transaction Data: {e}"
