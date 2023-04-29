"""This is a plugin to use Auto-GPT with Crypto."""
import ccxt
from web3 import Web3, HTTPProvider
import json
import requests
import asyncio
import os
from eth_abi.exceptions import DecodingError
from eth_abi.packed import encode_packed
from eth_account import Account
from typing import Any, Dict, List, Optional, Tuple, TypeVar, TypedDict
from auto_gpt_plugin_template import AutoGPTPluginTemplate
from uniswap import Uniswap
from telethon import TelegramClient
from .nfts import get_my_nfts, get_nfts, get_nft_of_the_day, get_eth_nft_metadata, get_arbitrum_nft_metadata, get_avalanche_nft_metadata, get_bsc_nft_metadata, get_fantom_nft_metadata, get_optimism_nft_metadata, get_polygon_nft_metadata, get_syscoin_nft_metadata

PromptGenerator = TypeVar("PromptGenerator")

infura_api = os.getenv('INFURA_API_KEY')
my_address = os.getenv('ETH_WALLET_ADDRESS')
mnemonic_phrase = os.getenv('ETH_WALLET_PRIVATE_KEY')
etherscan_api = os.getenv('ETHERSCAN_API_KEY')
lunarcrush_api = os.getenv('LUNARCRUSH_API_KEY')
telegram_api_id = os.getenv('TELEGRAM_API_ID')
telegram_api_hash = os.getenv('TELEGRAM_API_HASH')
kraken_api = os.getenv('KRAKEN_API_KEY')
kraken_secret = os.getenv('KRAKEN_SECRET')
coinbase_api = os.getenv('COINBASE_API_KEY')
coinbase_secret = os.getenv('COINBASE_SECRET')
network = os.getenv('ETH_NETWORK')
exchanges = os.getenv('CRYPTO_EXCHANGES')
endpoint = f"https://{network}.infura.io/v3/{infura_api}"

# Connect to Ethereum node using Infura
w3 = Web3(HTTPProvider(endpoint))

Account.enable_unaudited_hdwallet_features()


class Message(TypedDict):
    role: str
    content: str


class AutoGPTCryptoPlugin(AutoGPTPluginTemplate):
    """
    This is a plugin to use Auto-GPT with Crypto.
    """

    def __init__(self):
        super().__init__()
        self._name = "Auto-GPT-Crypto"
        self._version = "0.1.0"
        self._description = "This is a plugin for Auto-GPT-Crypto."
        self.client = TelegramClient(
            'Auto-GPT Crypto', telegram_api_id, telegram_api_hash)

        async def start_telegram():
            print('Starting Telegram Listener...')
            await self.client.start()

        self.client.loop.run_until_complete(start_telegram())

    def post_prompt(self, prompt: PromptGenerator) -> PromptGenerator:

        prompt.add_command(
            "Send ETH",
            "send_eth",
            {
                "recipient_address": "<recipient_address>",
                "amount": "<amount>",
                "private_key": "<private_key>"
            },
            self.send_eth
        ),
        prompt.add_command(
            "Create Wallet",
            "create_wallet",
            {},
            self.create_wallet
        ),
        prompt.add_command(
            "Swap Tokens",
            "swap_tokens",
            {
                "private_key": "<private_key",
                "token_address_in": "<token_address_in>",
                "token_address_out": "<token_address_out>",
                "amount": "<amount>"
            },
            self.swap_tokens
        ),
        prompt.add_command(
            "Get Coin of The Day",
            "get_coin_of_the_day",
            {},
            self.get_coin_of_the_day
        ),
        prompt.add_command(
            "Get NFT of The Day",
            "get_nft_of_the_day",
            {},
            self.get_nft_of_the_day_wrapper
        ),
        prompt.add_command(
            "Available Crypto Exchanges",
            "available_crypto_exchanges",
            {},
            self.available_crypto_exchanges
        ),
        prompt.add_command(
            "Balance on Kraken",
            "balance_on_kraken",
            {
                "symbol": "<symbol>"
            },
            self.balance_on_kraken
        ),
        prompt.add_command(
            "Balance on Coinbase",
            "balance_on_coinbase",
            {
                "symbol": "<symbol>"
            },
            self.balance_on_coinbase
        ),
        prompt.add_command(
            "Get My NFT's",
            "get_my_nfts",
            {},
            self.get_my_nfts_wrapper
        ),
        prompt.add_command(
            "Get NFT's",
            "get_nfts",
            {
                "wallet_address": "<wallet_address>"
            },
            self.get_nfts_wrapper
        ),
        prompt.add_command(
            "Get ETH NFT Metadata",
            "get_eth_nft_metadata",
            {
                "contract_address": "<contract_address>",
                "token_id": "<token_id>"
            },
            self.get_eth_nft_metadata_wrapper
        ),
        prompt.add_command(
            "Get BSC NFT Metadata",
            "get_bsc_nft_metadata",
            {
                "contract_address": "<contract_address>",
                "token_id": "<token_id>"
            },
            self.get_bsc_nft_metadata_wrapper
        ),
        prompt.add_command(
            "Get Polygon NFT Metadata",
            "get_polygon_nft_metadata",
            {
                "contract_address": "<contract_address>",
                "token_id": "<token_id>"
            },
            self.get_polygon_nft_metadata_wrapper
        ),
        prompt.add_command(
            "Get Arbitrum NFT Metadata",
            "get_arbitrum_nft_metadata",
            {
                "contract_address": "<contract_address>",
                "token_id": "<token_id>"
            },
            self.get_arbitrum_nft_metadata_wrapper
        ),
        prompt.add_command(
            "Get Avalanche NFT Metadata",
            "get_avalanche_nft_metadata",
            {
                "contract_address": "<contract_address>",
                "token_id": "<token_id>"
            },
            self.get_avalanche_nft_metadata_wrapper
        ),
        prompt.add_command(
            "Get Fantom NFT Metadata",
            "get_fantom_nft_metadata",
            {
                "contract_address": "<contract_address>",
                "token_id": "<token_id>"
            },
            self.get_fantom_nft_metadata_wrapper
        ),
        prompt.add_command(
            "Get Optimism NFT Metadata",
            "get_optimism_nft_metadata",
            {
                "contract_address": "<contract_address>",
                "token_id": "<token_id>"
            },
            self.get_optimism_nft_metadata_wrapper
        ),
        prompt.add_command(
            "Get Syscoin NFT Metadata",
            "get_syscoin_nft_metadata",
            {
                "contract_address": "<contract_address>",
                "token_id": "<token_id>"
            },
            self.get_syscoin_nft_metadata_wrapper
        ),
        prompt.add_command(
            "Get My ETH Balance",
            "get_my_eth_balance",
            {},
            self.get_my_eth_balance
        ),
        prompt.add_command(
            "Get ETH Balance",
            "get_eth_balance",
            {
                "address": "<address>"
            },
            self.get_eth_balance
        ),
        prompt.add_command(
            "Get ETH Token Balances",
            "get_eth_token_balances",
            {
                "wallet_address": "<wallet_address>"
            },
            self.get_eth_token_balances
        ),
        prompt.add_command(
            "Get Polygon Token Balances",
            "get_polygon_token_balances",
            {
                "wallet_address": "<wallet_address>"
            },
            self.get_polygon_token_balances
        ),
        prompt.add_command(
            "Get BSC Token Balances",
            "get_bsc_token_balances",
            {
                "wallet_address": "<wallet_address>"
            },
            self.get_bsc_token_balances
        ),
        prompt.add_command(
            "Get Avalanche Token Balances",
            "get_avalanche_token_balances",
            {
                "wallet_address": "<wallet_address>"
            },
            self.get_avalanche_token_balances
        ),
        prompt.add_command(
            "Get Syscoin Token Balances",
            "get_syscoin_token_balances",
            {
                "wallet_address": "<wallet_address>"
            },
            self.get_syscoin_token_balances
        ),
        prompt.add_command(
            "Get Arbitrum Token Balances",
            "get_arbitrum_token_balances",
            {
                "wallet_address": "<wallet_address>"
            },
            self.get_arbitrum_token_balances
        ),
        prompt.add_command(
            "Get Optimism Token Balances",
            "get_optimism_token_balances",
            {
                "wallet_address": "<wallet_address>"
            },
            self.get_optimism_token_balances
        ),
        prompt.add_command(
            "Stake Tokens",
            "stake_tokens",
            {
                "token_address": "<token_address>",
                "staking_contract_address": "<staking_contract_address>",
                "amount": "<amount>"
            },
            self.stake_tokens
        ),
        prompt.add_command(
            "Send Tokens",
            "send_tokens",
            {
                "token_address": "<token_address>",
                "recipient_address": "<recipient_address>",
                "amount": "<amount>"
            },
            self.send_tokens
        ),

        prompt.add_command(
            "Find New ETH Tokens",
            "find_new_eth_tokens",
            {},
            self.find_new_eth_tokens_wrapper
        )
        prompt.add_command(
            "Find Telegram Chat Messages",
            "find_telegram_chat_messages",
            {
                "chat_name": "<chat_name>"
            },
            self.find_telegram_chat_messages_wrapper
        )

        return prompt

    def can_handle_post_prompt(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_prompt method.
        Returns:
            bool: True if the plugin can handle the post_prompt method."""
        return True

    def can_handle_on_response(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_response method.
        Returns:
            bool: True if the plugin can handle the on_response method."""
        return False

    def on_response(self, response: str, *args, **kwargs) -> str:
        """This method is called when a response is received from the model."""
        pass

    def can_handle_on_planning(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_planning method.
        Returns:
            bool: True if the plugin can handle the on_planning method."""
        return False

    def on_planning(
        self, prompt: PromptGenerator, messages: List[Message]
    ) -> Optional[str]:
        """This method is called before the planning chat completion is done.
        Args:
            prompt (PromptGenerator): The prompt generator.
            messages (List[str]): The list of messages.
        """
        pass

    def can_handle_post_planning(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_planning method.
        Returns:
            bool: True if the plugin can handle the post_planning method."""
        return False

    def post_planning(self, response: str) -> str:
        """This method is called after the planning chat completion is done.
        Args:
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_instruction method.
        Returns:
            bool: True if the plugin can handle the pre_instruction method."""
        return False

    def pre_instruction(self, messages: List[Message]) -> List[Message]:
        """This method is called before the instruction chat is done.
        Args:
            messages (List[Message]): The list of context messages.
        Returns:
            List[Message]: The resulting list of messages.
        """
        pass

    def can_handle_on_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_instruction method.
        Returns:
            bool: True if the plugin can handle the on_instruction method."""
        return False

    def on_instruction(self, messages: List[Message]) -> Optional[str]:
        """This method is called when the instruction chat is done.
        Args:
            messages (List[Message]): The list of context messages.
        Returns:
            Optional[str]: The resulting message.
        """
        pass

    def can_handle_post_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_instruction method.
        Returns:
            bool: True if the plugin can handle the post_instruction method."""
        return False

    def post_instruction(self, response: str) -> str:
        """This method is called after the instruction chat is done.
        Args:
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_command method.
        Returns:
            bool: True if the plugin can handle the pre_command method."""
        return False

    def pre_command(
        self, command_name: str, arguments: Dict[str, Any]
    ) -> Tuple[str, Dict[str, Any]]:
        """This method is called before the command is executed.
        Args:
            command_name (str): The command name.
            arguments (Dict[str, Any]): The arguments.
        Returns:
            Tuple[str, Dict[str, Any]]: The command name and the arguments.
        """
        pass

    def can_handle_post_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_command method.
        Returns:
            bool: True if the plugin can handle the post_command method."""
        return False

    def post_command(self, command_name: str, response: str) -> str:
        """This method is called after the command is executed.
        Args:
            command_name (str): The command name.
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_chat_completion(
        self, messages: Dict[Any, Any], model: str, temperature: float, max_tokens: int
    ) -> bool:
        """This method is called to check that the plugin can
          handle the chat_completion method.
        Args:
            messages (List[Message]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.
          Returns:
              bool: True if the plugin can handle the chat_completion method."""
        return False

    def handle_chat_completion(
        self, messages: List[Message], model: str, temperature: float, max_tokens: int
    ) -> str:
        """This method is called when the chat completion is done.
        Args:
            messages (List[Message]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.
        Returns:
            str: The resulting response.
        """
        pass

################################################################################
# CRYPTO WALLET INTERACTIONS
################################################################################

    def create_wallet(self):
        # Generate a new Ethereum account with a mnemonic phrase
        acct, mnemonic = Account.create_with_mnemonic()

        # Save the address, private key, and mnemonic as a JSON object
        wallet = {
            "address": acct.address,
            "private_key": acct.key.hex(),
            "mnemonic": mnemonic
        }

        return wallet

    def get_eth_balance(self, address: str) -> float:
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getBalance",
            "params": [address, "latest"],
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

    def get_my_eth_balance(self) -> float:
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

    def send_eth(self, recipient_address: str, private_key: str, amount: float) -> str:
        # Set up a Web3 instance using an Infura provider
        w3 = Web3(Web3.HTTPProvider(endpoint))

        # Get the sender's account from the private key
        sender_account = Account.from_key(private_key)

        # Check if the sender has enough balance
        sender_balance = w3.eth.get_balance(sender_account.address)
        amount_wei = w3.to_wei(amount, 'ether')
        if sender_balance < amount_wei:
            return f"Insufficient balance."

        # Get the current nonce for the sender's address
        nonce = w3.eth.get_transaction_count(sender_account.address)

        # Prepare the transaction
        transaction = {
            'to': recipient_address,
            'value': amount_wei,
            'gas': 21000,
            'gasPrice': w3.eth.gas_price,
            'nonce': nonce,
            'chainId': w3.eth.chain_id,
        }

        # Sign the transaction
        signed_transaction = sender_account.sign_transaction(transaction)

        # Send the transaction
        transaction_hash = w3.eth.send_raw_transaction(
            signed_transaction.rawTransaction)

        return f"Transaction sent. Transaction hash: {transaction_hash.hex()}"

    def swap_tokens(self, private_key: str, token_address_in: str, token_address_out: str, amount_in: float, slippage: float) -> str:
        w3 = Web3(Web3.HTTPProvider(endpoint))
        account = Account.from_key(private_key)
        address = account.address
        uniswap_wrapper = Uniswap(
            address=address, private_key=private_key, version=2, web3=w3)

        # Calculate the minimum amount of output tokens you want to receive
        amount_out_min = int(amount_in * (1 - slippage))

        # Set the deadline (in seconds)
        deadline = w3.eth.getBlock('latest')['timestamp'] + 180  # 3 minutes from now

        # Approve the Uniswap router to spend your input tokens if needed
        token_in = w3.eth.contract(address=token_address_in, abi=ERC20_ABI)
        spender = uniswap_wrapper.router_address

        allowance = token_in.functions.allowance(address, spender).call()
        if allowance < amount_in:
            approve_tx = token_in.functions.approve(spender, w3.toWei('1000000000', 'ether')).buildTransaction({
                'from': address,
                'gas': 250000,
                'gasPrice': w3.toWei('5', 'gwei'),
                'nonce': w3.eth.getTransactionCount(address),
            })
            signed_tx = account.sign_transaction(approve_tx)
            w3.eth.sendRawTransaction(signed_tx.rawTransaction)

        # Swap tokens
        tx_hash = uniswap_wrapper.make_trade(
            TOKEN_IN_ADDRESS, TOKEN_OUT_ADDRESS, AMOUNT_IN, amount_out_min, deadline)
        print(f'Swap transaction sent: {tx_hash}')

    def get_eth_token_balances(self, wallet_address: str) -> dict:
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

    def get_polygon_token_balances(self, wallet_address: str) -> dict:
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

    def get_bsc_token_balances(self, wallet_address: str) -> dict:
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

    def get_fantom_token_balances(self, wallet_address: str) -> dict:
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

    def get_avalanche_token_balances(self, wallet_address: str) -> dict:
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

    def get_arbitrum_token_balances(self, wallet_address: str) -> dict:
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

    def get_syscoin_token_balances(self, wallet_address: str) -> dict:
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

    def get_optimism_token_balances(self, wallet_address: str) -> dict:
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

    def send_tokens(token_address: str, recipient_address: str, amount: float) -> str:
        api_endpoint = f'https://api.etherscan.io/api?module=contract&action=getabi&address={token_address}&apikey={etherscan_api}'

        # Send the API request to get the contract ABI
        try:
            response = requests.get(api_endpoint)
            response_json = response.json()
            if response_json['status'] != '1':
                return f"API error: {response_json['message']}"
            contract_abi = response_json['result']
        except Exception as e:
            return f"API request failed: {e}"

        # Convert amount to token units
        try:
            contract = w3.eth.contract(
                address=token_address, abi=contract_abi)
            token_decimals = contract.functions.decimals().call()
            amount_units = int(amount * 10 ** token_decimals)
        except Exception as e:
            return f"Failed to convert amount to token units: {e}"

        # Build transaction data
        try:
            transfer_data = encode_abi(
                '(address,uint256)', (recipient_address, amount_units))
            tx_data = contract.functions.transfer(recipient_address, amount_units).buildTransaction({
                'nonce': w3.eth.getTransactionCount(my_address),
                'gas': 200000,
                'gasPrice': w3.toWei('50', 'gwei'),
                'data': transfer_data
            })
        except Exception as e:
            return f"Failed to build transaction data: {e}"

        # Sign transaction
        try:
            signed_tx = w3.eth.account.sign_transaction(
                tx_data, private_key=private_key)
        except Exception as e:
            return f"Failed to sign transaction: {e}"

        # Send transaction
        try:
            tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        except Exception as e:
            return f"Failed to send transaction: {e}"

        # Get the token symbol
        try:
            token_symbol = contract.functions.symbol().call()
        except Exception as e:
            return f"Failed to get token symbol: {e}"

        return f"{amount} {token_symbol} tokens sent from {my_address} to {recipient_address}; transaction hash: {tx_hash.hex()}"

    def stake_tokens(token_address: str, staking_contract_address: str, sender_address: str, amount: float) -> str:
        # Connect to Ethereum network
        w3 = Web3(Web3.HTTPProvider(
            'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

        # Set the Etherscan API key and endpoint
        api_key = 'YOUR_ETHERSCAN_API_KEY'
        api_endpoint = f'https://api.etherscan.io/api?module=contract&action=getabi&address={token_address}&apikey={api_key}'

        # Send the API request to get the contract ABI
        try:
            response = requests.get(api_endpoint)
            response_json = response.json()
            if response_json['status'] != '1':
                return f"API error: {response_json['message']}"
            contract_abi = response_json['result']
        except Exception as e:
            return f"API request failed: {e}"

        # Convert amount to token units
        try:
            contract = w3.eth.contract(
                address=token_address, abi=contract_abi)
            token_decimals = contract.functions.decimals().call()
            amount_units = int(amount * 10 ** token_decimals)
        except Exception as e:
            return f"Failed to convert amount to token units: {e}"

        # Build transaction data
        try:
            approve_data = encode_packed(['address', 'uint256'], [
                staking_contract_address, amount_units])
            contract.functions.approve(staking_contract_address, amount_units).buildTransaction({
                'from': sender_address,
                'nonce': w3.eth.getTransactionCount(sender_address),
                'gas': 200000,
                'gasPrice': w3.toWei('50', 'gwei'),
                'data': approve_data.hex()
            })
            stake_data = encode_packed(['uint256'], [amount_units])
            staking_contract = w3.eth.contract(
                address=staking_contract_address, abi=staking_contract_abi)
            tx_data = staking_contract.functions.stake(amount_units).buildTransaction({
                'from': sender_address,
                'nonce': w3.eth.getTransactionCount(sender_address),
                'gas': 200000,
                'gasPrice': w3.toWei('50', 'gwei'),
                'data': stake_data.hex()
            })
        except Exception as e:
            return f"Failed to build transaction data: {e}"

        # Sign transaction
        try:
            signed_tx = w3.eth.account.sign_transaction(
                tx_data, private_key=private_key)
        except Exception as e:
            return f"Failed to sign transaction: {e}"

        # Send transaction
        try:
            tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        except Exception as e:
            return f"Failed to send transaction: {e}"

        # Get the token symbol
        try:
            token_symbol = contract.functions.symbol().call()
        except Exception as e:
            return f"Failed to get token symbol: {e}"

        return f"{amount} {token_symbol} tokens staked in contract {staking_contract_address}; transaction hash: {tx_hash}"

################################################################################
# LUNARCRUSH
################################################################################

    def get_coin_of_the_day(self) -> float:

        url = "https://lunarcrush.com/api3/coinoftheday"
        headers = {
            'Authorization': f'Bearer {lunarcrush_api}'
        }

        response = requests.request("GET", url, headers=headers)

        if response.status_code == 200:
            return response.text.encode('utf8')
        else:
            raise Exception(
                f"Failed to get coin of the day from LunarCrush; status code {response.status_code}")

################################################################################
# NFTS
################################################################################
    def get_nfts_wrapper(self, wallet_address: str) -> str:
        nfts = get_nfts(wallet_address)
        return nfts

    def get_my_nfts_wrapper(self, wallet_address: str) -> str:
        nfts = get_my_nfts(wallet_address)
        return nfts

    def get_nft_of_the_day_wrapper(self) -> str:
        data = get_nft_of_the_day(lunarcrush_api)
        return data

    def get_eth_nft_metadata_wrapper(self, contract_address: str, token_id: str) -> str:
        data = get_eth_nft_metadata(contract_address, token_id)
        return data

    def get_bsc_nft_metadata_wrapper(self, contract_address: str, token_id: str) -> str:
        data = get_bsc_nft_metadata(contract_address, token_id)
        return data

    def get_polygon_nft_metadata_wrapper(self, contract_address: str, token_id: str) -> str:
        data = get_polygon_nft_metadata(contract_address, token_id)
        return data

    def get_arbitrum_nft_metadata_wrapper(self, contract_address: str, token_id: str) -> str:
        data = get_arbitrum_nft_metadata(contract_address, token_id)
        return data

    def get_avalanche_nft_metadata_wrapper(self, contract_address: str, token_id: str) -> str:
        data = get_avalanche_nft_metadata(contract_address, token_id)
        return data

    def get_fantom_nft_metadata_wrapper(self, contract_address: str, token_id: str) -> str:
        data = get_fantom_nft_metadata(contract_address, token_id)
        return data

    def get_optimism_nft_metadata_wrapper(self, contract_address: str, token_id: str) -> str:
        data = get_optimism_nft_metadata(contract_address, token_id)
        return data

    def get_syscoin_nft_metadata_wrapper(self, contract_address: str, token_id: str) -> str:
        data = get_syscoin_nft_metadata(contract_address, token_id)
        return data

################################################################################
# TELEGRAM
################################################################################

    def find_new_eth_tokens_wrapper(self):
        # Run the coroutine and return the result
        return self.client.loop.run_until_complete(self.find_new_eth_tokens())

    def find_telegram_chat_messages_wrapper(self):
        # Run the coroutine and return the result
        return self.client.loop.run_until_complete(self.find_telegram_chat_messages())

    async def find_new_eth_tokens(self) -> List[str]:
        entity = await self.client.get_entity('DEXTNewPairsBot')
        messages = await self.client.get_messages(entity, 20)
        messages_list = []  # Create an empty list to store messages

        for message in messages:
            messages_list.append(str(message.message))

        # Convert the messages_list to a JSON string
        messages_json = json.dumps(messages_list)
        return messages_json

    async def find_telegram_chat_messages(self, chat_name: str) -> List[str]:
        entity = await self.client.get_entity(chat_name)
        messages = await self.client.get_messages(entity, 20)
        messages_list = []  # Create an empty list to store messages

        for message in messages:
            messages_list.append(str(message.message))

        # Convert the messages_list to a JSON string
        messages_json = json.dumps(messages_list)
        return messages_json

################################################################################
# EXCHANGE TRADING
################################################################################

    def available_crypto_exchanges(self) -> str:
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

    def balance_on_kraken(self) -> str:
        try:
            kraken = ccxt.kraken({
                'apiKey': kraken_api,
                'secret': kraken_secret,
            })
            balance = kraken.fetch_balance()

            return balance
        except Exception as e:
            return f"An error occurred while retrieving balance from Kraken: {str(e)}"

    def balance_on_coinbase(self) -> str:
        try:
            coinbase = ccxt.coinbase({
                'apiKey': coinbase_api,
                'secret': coinbase_secret,
            })
            balance = coinbase.fetch_balance()

            return balance
        except Exception as e:
            return f"An error occurred while retrieving balance from Coinbase: {str(e)}"
