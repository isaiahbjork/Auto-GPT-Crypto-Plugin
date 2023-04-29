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

            # Convert Wei to Ether
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
            return f"Failed to get ETH NFT Metadata: {e}"
