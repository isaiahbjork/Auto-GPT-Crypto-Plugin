"""This is a plugin to use Auto-GPT with Crypto."""
# 1. CRYPTO WALLET INTERACTIONS
# 2. BALANCES
# 3. NFTS
# 4. TRANSACTIONS
# 5. EXCHANGE TRADING
# 6. TELEGRAM
# 7. LUNARCRUSH
# 8. FCS
# 9. COINMARKETCAP

from web3 import Web3, HTTPProvider
import os
from typing import Any, Dict, List, Optional, Tuple, TypeVar, TypedDict
from auto_gpt_plugin_template import AutoGPTPluginTemplate
from uniswap import Uniswap
from telethon import TelegramClient
from .nfts import Nfts
from .transactions import Transactions
from .lunarcrush import LunarCrush
from .exchanges import Exchanges
from .balances import Balances
from .wallet import Wallet
from .telegram import Telegram
from .fcs import Fcs
from .coinmarketcap import CoinMarketCap

PromptGenerator = TypeVar("PromptGenerator")

infura_api = os.getenv('INFURA_API_KEY')
my_address = os.getenv('ETH_WALLET_ADDRESS')
my_private_key = os.getenv('ETH_WALLET_PRIVATE_KEY')
etherscan_api = os.getenv('ETHERSCAN_API_KEY')
lunarcrush_api = os.getenv('LUNARCRUSH_API_KEY')
telegram_api_id = os.getenv('TELEGRAM_API_ID')
telegram_api_hash = os.getenv('TELEGRAM_API_HASH')
kraken_api = os.getenv('KRAKEN_API_KEY')
kraken_secret = os.getenv('KRAKEN_SECRET')
coinbase_api = os.getenv('COINBASE_API_KEY')
coinbase_secret = os.getenv('COINBASE_SECRET')
fcs_api = os.getenv('FCS_API_KEY')
cmc_api = os.getenv('CMC_API_KEY')
endpoint = f"https://rpc.ankr.com/"

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

    def post_prompt(self, prompt: PromptGenerator) -> PromptGenerator:
       # 1. CRYPTO WALLET INTERACTIONS
        prompt.add_command(
            "Send ETH",
            "send_eth",
            {
                "recipient_address": "<recipient_address>",
                "amount": "<amount>",
                "private_key": "<private_key>"
            },
            self.send_eth_wrapper
        ),
        prompt.add_command(
            "Send Matic",
            "send_matic",
            {
                "recipient_address": "<recipient_address>",
                "amount": "<amount>",
                "private_key": "<private_key>"
            },
            self.send_matic_wrapper
        ),
        prompt.add_command(
            "Stake Matic",
            "stake_matic",
            {
                "amount": "<amount>",
                "private_key": "<private_key>"
            },
            self.stake_matic_wrapper
        ),
        prompt.add_command(
            "Create Wallet",
            "create_wallet",
            {},
            self.create_wallet_wrapper
        ),
        prompt.add_command(
            "Get My Wallet Info",
            "get_my_wallet_info",
            {},
            self.get_my_wallet_info_wrapper
        ),
        # prompt.add_command(
        #     "Swap Tokens",
        #     "swap_tokens",
        #     {
        #         "private_key": "<private_key",
        #         "token_address_in": "<token_address_in>",
        #         "token_address_out": "<token_address_out>",
        #         "amount": "<amount>"
        #     },
        #     self.swap_tokens
        # ),
        # prompt.add_command(
        #     "Stake Tokens",
        #     "stake_tokens",
        #     {
        #         "token_address": "<token_address>",
        #         "staking_contract_address": "<staking_contract_address>",
        #         "amount": "<amount>"
        #     },
        #     self.stake_tokens
        # ),
        # prompt.add_command(
        #     "Send Tokens",
        #     "send_tokens",
        #     {
        #         "token_address": "<token_address>",
        #         "recipient_address": "<recipient_address>",
        #         "amount": "<amount>"
        #     },
        #     self.send_tokens
        # ),
        # 2. BALANCES
        prompt.add_command(
            "Get My ETH Balance",
            "get_my_eth_balance",
            {},
            self.get_my_eth_balance_wrapper
        ),
        prompt.add_command(
            "Get ETH Balance",
            "get_eth_balance",
            {
                "wallet_address": "<wallet_address>"
            },
            self.get_eth_balance_wrapper
        ),
        prompt.add_command(
            "Get ETH Token Balances",
            "get_eth_token_balances",
            {
                "wallet_address": "<wallet_address>"
            },
            self.get_eth_token_balances_wrapper
        ),
        prompt.add_command(
            "Get Polygon Token Balances",
            "get_polygon_token_balances",
            {
                "wallet_address": "<wallet_address>"
            },
            self.get_polygon_token_balances_wrapper
        ),
        prompt.add_command(
            "Get BSC Token Balances",
            "get_bsc_token_balances",
            {
                "wallet_address": "<wallet_address>"
            },
            self.get_bsc_token_balances_wrapper
        ),
        prompt.add_command(
            "Get Fantom Token Balances",
            "get_fantom_token_balances",
            {
                "wallet_address": "<wallet_address>"
            },
            self.get_fantom_token_balances_wrapper
        ),
        prompt.add_command(
            "Get Avalanche Token Balances",
            "get_avalanche_token_balances",
            {
                "wallet_address": "<wallet_address>"
            },
            self.get_avalanche_token_balances_wrapper
        ),
        prompt.add_command(
            "Get Syscoin Token Balances",
            "get_syscoin_token_balances",
            {
                "wallet_address": "<wallet_address>"
            },
            self.get_syscoin_token_balances_wrapper
        ),
        prompt.add_command(
            "Get Arbitrum Token Balances",
            "get_arbitrum_token_balances",
            {
                "wallet_address": "<wallet_address>"
            },
            self.get_arbitrum_token_balances_wrapper
        ),
        prompt.add_command(
            "Get Optimism Token Balances",
            "get_optimism_token_balances",
            {
                "wallet_address": "<wallet_address>"
            },
            self.get_optimism_token_balances_wrapper
        ),
        # 3. NFTs
        prompt.add_command(
            "Get NFT of The Day",
            "get_nft_of_the_day",
            {},
            self.get_nft_of_the_day_wrapper
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
        # 4. TRANSACTIONS
        prompt.add_command(
            "Get ETH transaction data",
            "get_eth_transaction_data",
            {
                "transaction_hash": "<transaction_hash>"
            },
            self.get_eth_transaction_data_wrapper
        ),
        prompt.add_command(
            "Get Polygon transaction data",
            "get_polygon_transaction_data",
            {
                "transaction_hash": "<transaction_hash>"
            },
            self.get_polygon_transaction_data_wrapper
        ),
        prompt.add_command(
            "Get BSC transaction data",
            "get_bsc_transaction_data",
            {
                "transaction_hash": "<transaction_hash>"
            },
            self.get_bsc_transaction_data_wrapper
        ),
        prompt.add_command(
            "Get Fantom transaction data",
            "get_fantom_transaction_data",
            {
                "transaction_hash": "<transaction_hash>"
            },
            self.get_fantom_transaction_data_wrapper
        ),
        prompt.add_command(
            "Get Arbitrum transaction data",
            "get_arbitrum_transaction_data",
            {
                "transaction_hash": "<transaction_hash>"
            },
            self.get_arbitrum_transaction_data_wrapper
        ),
        prompt.add_command(
            "Get Avalanche transaction data",
            "get_avalanche_transaction_data",
            {
                "transaction_hash": "<transaction_hash>"
            },
            self.get_avalanche_transaction_data_wrapper
        ),
        prompt.add_command(
            "Get Optimism transaction data",
            "get_optimism_transaction_data",
            {
                "transaction_hash": "<transaction_hash>"
            },
            self.get_optimism_transaction_data_wrapper
        ),
        prompt.add_command(
            "Get Syscoin transaction data",
            "get_syscoin_transaction_data",
            {
                "transaction_hash": "<transaction_hash>"
            },
            self.get_syscoin_transaction_data_wrapper
        ),
        # 5. EXCHANGE TRADING
        prompt.add_command(
            "Available Crypto Exchanges",
            "available_crypto_exchanges",
            {},
            self.available_crypto_exchanges_wrapper
        ),
        prompt.add_command(
            "Balance on Kraken",
            "balance_on_kraken",
            {},
            self.balance_on_kraken_wrapper
        ),
        prompt.add_command(
            "Balance on Coinbase",
            "balance_on_coinbase",
            {},
            self.balance_on_coinbase_wrapper
        ),
        # 6. TELEGRAM
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
        ),
        # 7. LUNARCRUSH
        prompt.add_command(
            "Get Coin of The Day",
            "get_coin_of_the_day",
            {},
            self.get_coin_of_the_day_wrapper
        ),
        prompt.add_command(
            "Get Cryptos By Galaxy Score",
            "get_lunarcrush_galaxy_score_cryptos",
            {},
            self.get_lunarcrush_galaxy_score_cryptos_wrapper
        ),
        prompt.add_command(
            "Get Cryptos By Alt Rank",
            "get_lunarcrush_alt_rank_cryptos",
            {},
            self.get_lunarcrush_alt_rank_cryptos_wrapper
        ),
        prompt.add_command(
            "Get Recent Crypto Social Feeds",
            "get_recent_crypto_social_feeds",
            {},
            self.get_recent_crypto_social_feeds_wrapper
        ),
        # 8. FCS
        prompt.add_command(
            "Get Pivot Points Signals",
            "get_crypto_pivot_points",
            {
                "symbol": "<symbol>",
                "timeframe": "<timeframe>"
            },
            self.get_crypto_pivot_points_wrapper
        ),
        prompt.add_command(
            "Get Moving Average Signals",
            "get_crypto_moving_averages",
            {
                "symbol": "<symbol>",
                "timeframe": "<timeframe>"
            },
            self.get_crypto_moving_averages_wrapper
        ),
        prompt.add_command(
            "Get Technical Indicators Signals",
            "get_crypto_technical_indicators",
            {
                "symbol": "<symbol>",
                "timeframe": "<timeframe>"
            },
            self.get_crypto_technical_indicators_wrapper
        ),
        # 9. COINMARKETCAP
        prompt.add_command(
            "Get Upcoming Airdrops",
            "get_coinmarketcap_airdrops",
            {},
            self.get_coinmarketcap_airdrops_wrapper
        ),
        prompt.add_command(
            "Convert Crypto",
            "convert_crypto",
            {
                "amount": "<amount>",
                "symbol": "<symbol>",
                "conversion_symbol": "<conversion_symbol>"
            },
            self.convert_crypto_wrapper
        ),
        return prompt

    def can_handle_post_prompt(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_prompt method.
        Returns:
            bool: True if the plugin can handle the post_prompt method."""
        return True

################################################################################
# 1. CRYPTO WALLET INTERACTIONS
################################################################################
    def send_eth_wrapper(self, recipient_address: str, amount: float, private_key: str) -> str:
        data = Wallet.send_eth(recipient_address, private_key, amount, endpoint)
        return data
    
    def send_matic_wrapper(self, recipient_address: str, amount: float, private_key: str) -> str:
        data = Wallet.send_matic(recipient_address, private_key, amount, endpoint)
        return data
    
    def stake_matic_wrapper(self, amount: float, private_key: str) -> str:
        data = Wallet.stake_matic(amount, private_key, endpoint)
        return data
    
    def create_wallet_wrapper(self):
        data = Wallet.create_wallet()
        return data
    
    def get_my_wallet_info_wrapper(self):
        data = Wallet.get_my_wallet_info()
        return data

################################################################################
# 2. BALANCES
################################################################################


    def get_my_eth_balance_wrapper(self):
        data = Balances.get_my_eth_balance(my_address, endpoint)
        return data

    def get_eth_balance_wrapper(self, wallet_address: str) -> str:
        data = Balances.get_eth_balance(wallet_address, endpoint)
        return data

    def get_eth_token_balances_wrapper(self, wallet_address: str) -> str:
        data = Balances.get_eth_token_balances(wallet_address)
        return data

    def get_bsc_token_balances_wrapper(self, wallet_address: str) -> str:
        data = Balances.get_bsc_token_balances(wallet_address)
        return data

    def get_polygon_token_balances_wrapper(self, wallet_address: str) -> str:
        data = Balances.get_polygon_token_balances(wallet_address)
        return data

    def get_arbitrum_token_balances_wrapper(self, wallet_address: str) -> str:
        data = Balances.get_arbitrum_token_balances(wallet_address)
        return data

    def get_avalanche_token_balances_wrapper(self, wallet_address: str) -> str:
        data = Balances.get_avalanche_token_balances(wallet_address)
        return data

    def get_fantom_token_balances_wrapper(self, wallet_address: str) -> str:
        data = Balances.get_fantom_token_balances(wallet_address)
        return data

    def get_optimism_token_balances_wrapper(self, wallet_address: str) -> str:
        data = Balances.get_optimism_token_balances(wallet_address)
        return data

    def get_syscoin_token_balances_wrapper(self, wallet_address: str) -> str:
        data = Balances.get_syscoin_token_balances(wallet_address)
        return data

################################################################################
# 3. NFTS
################################################################################

    def get_nfts_wrapper(self, wallet_address: str) -> str:
        nfts = Nfts.get_nfts(wallet_address)
        return nfts

    def get_my_nfts_wrapper(self):
        nfts = Nfts.get_my_nfts(my_address)
        return nfts

    def get_nft_of_the_day_wrapper(self):
        data = Nfts.get_nft_of_the_day(lunarcrush_api)
        return data

    def get_eth_nft_metadata_wrapper(self, contract_address: str, token_id: str) -> str:
        data = Nfts.get_eth_nft_metadata(contract_address, token_id)
        return data

    def get_bsc_nft_metadata_wrapper(self, contract_address: str, token_id: str) -> str:
        data = Nfts.get_bsc_nft_metadata(contract_address, token_id)
        return data

    def get_polygon_nft_metadata_wrapper(self, contract_address: str, token_id: str) -> str:
        data = Nfts.get_polygon_nft_metadata(contract_address, token_id)
        return data

    def get_arbitrum_nft_metadata_wrapper(self, contract_address: str, token_id: str) -> str:
        data = Nfts.get_arbitrum_nft_metadata(contract_address, token_id)
        return data

    def get_avalanche_nft_metadata_wrapper(self, contract_address: str, token_id: str) -> str:
        data = Nfts.get_avalanche_nft_metadata(contract_address, token_id)
        return data

    def get_fantom_nft_metadata_wrapper(self, contract_address: str, token_id: str) -> str:
        data = Nfts.get_fantom_nft_metadata(contract_address, token_id)
        return data

    def get_optimism_nft_metadata_wrapper(self, contract_address: str, token_id: str) -> str:
        data = Nfts.get_optimism_nft_metadata(contract_address, token_id)
        return data

    def get_syscoin_nft_metadata_wrapper(self, contract_address: str, token_id: str) -> str:
        data = Nfts.get_syscoin_nft_metadata(contract_address, token_id)
        return data

################################################################################
# 4. TRANSACTIONS
################################################################################

    def get_eth_transaction_data_wrapper(self, transaction_hash: str) -> str:
        data = Transactions.get_eth_transaction_data(transaction_hash)
        return data

    def get_polygon_transaction_data_wrapper(self, transaction_hash: str) -> str:
        data = Transactions.get_polygon_transaction_data(transaction_hash)
        return data

    def get_bsc_transaction_data_wrapper(self, transaction_hash: str) -> str:
        data = Transactions.get_bsc_transaction_data(transaction_hash)
        return data

    def get_fantom_transaction_data_wrapper(self, transaction_hash: str) -> str:
        data = Transactions.get_fantom_transaction_data(transaction_hash)
        return data

    def get_fantom_transaction_data_wrapper(self, transaction_hash: str) -> str:
        data = Transactions.get_fantom_transaction_data(transaction_hash)
        return data

    def get_arbitrum_transaction_data_wrapper(self, transaction_hash: str) -> str:
        data = Transactions.get_arbitrum_transaction_data(transaction_hash)
        return data

    def get_avalanche_transaction_data_wrapper(self, transaction_hash: str) -> str:
        data = Transactions.get_avalanche_transaction_data(transaction_hash)
        return data

    def get_optimism_transaction_data_wrapper(self, transaction_hash: str) -> str:
        data = Transactions.get_optimism_transaction_data(transaction_hash)
        return data

    def get_syscoin_transaction_data_wrapper(self, transaction_hash: str) -> str:
        data = Transactions.get_syscoin_transaction_data(transaction_hash)
        return data

################################################################################
# 5. EXCHANGE TRADING
################################################################################

    def available_crypto_exchanges_wrapper(self):
        data = Exchanges.available_crypto_exchanges()
        return data

    def balance_on_coinbase_wrapper(self):
        data = Exchanges.balance_on_coinbase(coinbase_api, coinbase_secret)
        return data

    def balance_on_kraken_wrapper(self):
        data = Exchanges.balance_on_kraken(kraken_api, kraken_secret)
        return data

################################################################################
# 6. TELEGRAM
################################################################################

    def find_new_eth_tokens_wrapper(self):
        # Run the coroutine and return the result
        return self.client.loop.run_until_complete(Telegram.find_new_eth_tokens(self.client))

    def find_telegram_chat_messages_wrapper(self, chat_name: str) -> str:
        # Run the coroutine and return the result
        return self.client.loop.run_until_complete(Telegram.find_telegram_chat_messages(self.client, chat_name))

################################################################################
# 7. LUNARCRUSH
################################################################################

    def get_coin_of_the_day_wrapper(self):
        data = LunarCrush.get_coin_of_the_day(lunarcrush_api)
        return data
    
    def get_lunarcrush_galaxy_score_cryptos_wrapper(self):
        data = LunarCrush.get_lunarcrush_galaxy_score_cryptos(lunarcrush_api)
        return data
    
    def get_lunarcrush_alt_rank_cryptos_wrapper(self):
        data = LunarCrush.get_lunarcrush_alt_rank_cryptos(lunarcrush_api)
        return data

    def get_recent_crypto_social_feeds_wrapper(self):
        data = LunarCrush.get_recent_crypto_social_feeds(lunarcrush_api)
        return data

################################################################################
# 8. FCS
################################################################################

    def get_crypto_pivot_points_wrapper(self, symbol: str, timeframe: str) -> str:
        data = Fcs.get_crypto_pivot_points(fcs_api, symbol, timeframe)
        return data
    
    def get_crypto_moving_averages_wrapper(self, symbol: str, timeframe: str) -> str:
        data = Fcs.get_crypto_moving_averages(fcs_api, symbol, timeframe)
        return data
    
    def get_crypto_technical_indicators_wrapper(self, symbol: str, timeframe: str) -> str:
        data = Fcs.get_crypto_technical_indicators(fcs_api, symbol, timeframe)
        return data

################################################################################
# 9. COINMARKETCAP
################################################################################
    
    def get_coinmarketcap_airdrops_wrapper(self) -> str:
        data = CoinMarketCap.get_coinmarketcap_airdrops(cmc_api)
        return data
    
    def convert_crypto_wrapper(self, amount: float, symbol: str, conversion_symbol: str) -> str:
        data = CoinMarketCap.convert_crypto(cmc_api, amount, symbol, conversion_symbol)
        return data