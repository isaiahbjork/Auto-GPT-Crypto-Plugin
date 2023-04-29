import requests


def get_my_nfts(my_address):
    try:
        url = "https://rpc.ankr.com/multichain/?ankr_getNFTsByOwner="

        payload = {
            "jsonrpc": "2.0",
            "method": "ankr_getNFTsByOwner",
            "params": {
                "blockchain": [],
                "walletAddress": my_address,
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

        nft_info = []
        for asset in assets:
            blockchain = asset['blockchain']
            symbol = asset['symbol']
            contract_address = asset['contractAddress']
            name = asset['name']
            nft_info.append({'name': name, 'symbol': symbol,
                             'contract_address': contract_address, 'blockchain': blockchain})
        return nft_info

    except Exception as e:
        return f"Failed to get NFTs: {e}"

def get_nfts(wallet_address):
    try:
        url = "https://rpc.ankr.com/multichain/?ankr_getNFTsByOwner="

        payload = {
            "jsonrpc": "2.0",
            "method": "ankr_getNFTsByOwner",
            "params": {
                "blockchain": [],
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

        nft_info = []
        for asset in assets:
            blockchain = asset['blockchain']
            symbol = asset['symbol']
            contract_address = asset['contractAddress']
            name = asset['name']
            nft_info.append({'name': name, 'symbol': symbol,
                            'contract_address': contract_address, 'blockchain': blockchain})
        return nft_info

    except Exception as e:
        return f"Failed to get NFT's: {e}"

def get_nft_of_the_day(lunarcrush_api) -> float:

    url = "https://lunarcrush.com/api3/nftoftheday"
    headers = {
        'Authorization': f'Bearer {lunarcrush_api}'
    }

    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        return response.text.encode('utf8')
    else:
        raise Exception(
            f"Failed to get NFT of the day from LunarCrush; status code {response.status_code}")

def get_eth_nft_metadata(contract_address, token_id):
        try:
            url = "https://rpc.ankr.com/multichain/?ankr_getNFTMetadata="

            payload = {
                "jsonrpc": "2.0",
                "method": "ankr_getNFTMetadata",
                "params": {
                    "blockchain": "eth",
                    "contractAddress": contract_address,
                    "tokenId": token_id
                },
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            data = response_data

            return data

        except Exception as e:
            return f"Failed to get ETH NFT Metadata: {e}"

def get_bsc_nft_metadata(contract_address, token_id):
        try:
            url = "https://rpc.ankr.com/multichain/?ankr_getNFTMetadata="

            payload = {
                "jsonrpc": "2.0",
                "method": "ankr_getNFTMetadata",
                "params": {
                    "blockchain": "bsc",
                    "contractAddress": contract_address,
                    "tokenId": token_id
                },
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            data = response_data

            return data

        except Exception as e:
            return f"Failed to get BSC NFT Metadata: {e}"

def get_polygon_nft_metadata(contract_address, token_id):
        try:
            url = "https://rpc.ankr.com/multichain/?ankr_getNFTMetadata="

            payload = {
                "jsonrpc": "2.0",
                "method": "ankr_getNFTMetadata",
                "params": {
                    "blockchain": "polygon",
                    "contractAddress": contract_address,
                    "tokenId": token_id
                },
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            data = response_data

            return data

        except Exception as e:
            return f"Failed to get Polygon NFT Metadata: {e}"
        
def get_arbitrum_nft_metadata(contract_address, token_id):
        try:
            url = "https://rpc.ankr.com/multichain/?ankr_getNFTMetadata="

            payload = {
                "jsonrpc": "2.0",
                "method": "ankr_getNFTMetadata",
                "params": {
                    "blockchain": "arbitrum",
                    "contractAddress": contract_address,
                    "tokenId": token_id
                },
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            data = response_data

            return data

        except Exception as e:
            return f"Failed to get Arbitrum NFT Metadata: {e}"

def get_avalanche_nft_metadata(contract_address, token_id):
        try:
            url = "https://rpc.ankr.com/multichain/?ankr_getNFTMetadata="

            payload = {
                "jsonrpc": "2.0",
                "method": "ankr_getNFTMetadata",
                "params": {
                    "blockchain": "avalanche",
                    "contractAddress": contract_address,
                    "tokenId": token_id
                },
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            data = response_data

            return data

        except Exception as e:
            return f"Failed to get Avalanche NFT Metadata: {e}"
        
def get_fantom_nft_metadata(contract_address, token_id):
        try:
            url = "https://rpc.ankr.com/multichain/?ankr_getNFTMetadata="

            payload = {
                "jsonrpc": "2.0",
                "method": "ankr_getNFTMetadata",
                "params": {
                    "blockchain": "avalanche",
                    "contractAddress": contract_address,
                    "tokenId": token_id
                },
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            data = response_data

            return data

        except Exception as e:
            return f"Failed to get Fantom NFT Metadata: {e}"

def get_optimism_nft_metadata(contract_address, token_id):
        try:
            url = "https://rpc.ankr.com/multichain/?ankr_getNFTMetadata="

            payload = {
                "jsonrpc": "2.0",
                "method": "ankr_getNFTMetadata",
                "params": {
                    "blockchain": "avalanche",
                    "contractAddress": contract_address,
                    "tokenId": token_id
                },
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            data = response_data

            return data

        except Exception as e:
            return f"Failed to get Optimism NFT Metadata: {e}"

def get_syscoin_nft_metadata(contract_address, token_id):
        try:
            url = "https://rpc.ankr.com/multichain/?ankr_getNFTMetadata="

            payload = {
                "jsonrpc": "2.0",
                "method": "ankr_getNFTMetadata",
                "params": {
                    "blockchain": "syscoin",
                    "contractAddress": contract_address,
                    "tokenId": token_id
                },
                "id": 1
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            data = response_data

            return data

        except Exception as e:
            return f"Failed to get Syscoin NFT Metadata: {e}"