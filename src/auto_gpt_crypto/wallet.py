import os
import requests
import json
from web3 import Web3, HTTPProvider
from eth_account import Account
from eth_utils import to_checksum_address
from web3.middleware import geth_poa_middleware

Account.enable_unaudited_hdwallet_features()

address = os.getenv('ETH_WALLET_ADDRESS')
private_key = os.getenv('ETH_WALLET_PRIVATE_KEY')
etherscan = os.getenv('ETHERSCAN_API_KEY')
polyscan = os.getenv('POLYSCAN_API_KEY')


class Wallet():

    def create_wallet():
        # Generate a new Ethereum account with a mnemonic phrase
        acct, mnemonic = Account.create_with_mnemonic()

        # Save the address, private key, and mnemonic as a JSON object
        wallet = {
            "address": acct.address,
            "private_key": acct.key.hex(),
            "mnemonic": mnemonic
        }

        return wallet

    def get_my_wallet_info():
        wallet = {
            "address": address,
            "private_key": private_key
        }
        return wallet

    def send_eth(recipient_address, private_key, amount, endpoint):
        # Set up a Web3 instance using an Web3 provider
        w3 = Web3(Web3.HTTPProvider(f'{endpoint}/eth'))
        amount = float(amount)
        # Get the sender's account from the private key
        sender_account = Account.from_key(private_key)

        # Check if the sender has enough balance
        sender_balance = w3.eth.get_balance(sender_account.address)
        sender_balance = float(sender_balance)
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

        return f"ETH Transaction sent. Transaction hash: {transaction_hash.hex()}"

    def send_matic(recipient_address, private_key, amount, endpoint):
        # Set up a Web3 instance using an Web3 provider
        w3 = Web3(Web3.HTTPProvider(f'{endpoint}/polygon'))
        amount = float(amount)
        # Get the sender's account from the private key
        sender_account = Account.from_key(private_key)

        # Check if the sender has enough balance
        sender_balance = w3.eth.get_balance(sender_account.address)
        sender_balance = float(sender_balance)
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

        return f"Matic Transaction sent. Transaction hash: {transaction_hash.hex()}"

    def swap_matic_for_tokens(token_address, private_key, amount, endpoint):
        w3 = Web3(Web3.HTTPProvider(f'{endpoint}/polygon'))

        # Set up account information
        sender_account = Account.from_key(private_key)
        sender_address = sender_account.address

        # Add the geth_poa_middleware
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)

        # Get the current gas price from the Ethereum network
        gas_price = w3.eth.gas_price

        # Add a little extra gas price to ensure the transaction goes through
        adjusted_gas_price = int(gas_price * 1.2)

        amount = float(amount)
        quickswap_address = '0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff'

        # Get the QuickSwap contract ABI
        url = "https://api.polygonscan.com/api"
        params = {
            "module": "contract",
            "action": "getabi",
            "address": quickswap_address,
            "apikey": polyscan
        }

        response = requests.get(url, params=params)
        data = response.json()

        if data["status"] == "1":
            # Set up QuickSwap contract and relevant addresses
            quickswap_router = w3.eth.contract(
                address=quickswap_address, abi=data['result'])

            # Set up token addresses
            matic_address = '0x0000000000000000000000000000000000001010'

            # Set up swap parameters
            amount_in = Web3.to_wei(amount, 'ether')  # Amount of Matic to swap (in wei)
            amount_out_min = 1  # Minimum amount of PolyDoge to receive (in wei)
            deadline = int(w3.eth.get_block('latest').timestamp +
                           300)  # Transaction deadline in Unix time

            # Get the current nonce for the sender's address
            nonce = w3.eth.get_transaction_count(sender_address)
            url = "https://api.polygonscan.com/api"
            params = {
                "module": "contract",
                "action": "getabi",
                "address": token_address,
                "apikey": polyscan
            }

            response = requests.get(url, params=params)
            data1 = response.json()

            if data1["status"] == "1":
                token_contract = w3.eth.contract(
                    address=token_address, abi=data1['result'])
                matic_reserve, token_reserve = quickswap_router.functions.getReserves().call()
                token_amount_in = token_contract.functions.balanceOf(
                    sender_address).call()
                matic_amount_in = quickswap_router.functions.getAmountIn(
                    token_amount_in, token_reserve, matic_reserve).call()
                if matic_amount_in > w3.eth.get_balance(sender_address):
                    return "Insufficient Matic balance."
                if token_amount_in > token_contract.functions.allowance(sender_address, quickswap_address).call():
                    return "Token allowance too low."
                if token_amount_in > token_contract.functions.balanceOf(sender_address).call():
                    return "Insufficient token balance."
                if amount_in > matic_amount_in:
                    return "Insufficient liquidity in the pool."

                # Set up the swap transaction
                swap_tx = quickswap_router.functions.swapExactTokensForTokens(
                    amount_in,
                    amount_out_min,
                    [matic_address, token_address],
                    sender_address,
                    deadline
                ).build_transaction({
                    'from': sender_address,
                    'nonce': nonce,
                    'gasPrice': adjusted_gas_price,
                    'gas': 1000000,
                })

                # Sign the transaction
                signed_tx = sender_account.sign_transaction(swap_tx)

                # Send the transaction
                tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

                # Wait for the transaction to be confirmed
                receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

                # Check the transaction status
                if receipt['status'] == 1:
                    return f"Swap successful. Transaction hash: {tx_hash.hex()}"
                else:
                    return f"Swap failed. Transaction hash: {tx_hash.hex()}"

    def stake_matic(amount, private_key, endpoint):
        w3 = Web3(Web3.HTTPProvider(f'{endpoint}/polygon'))
        staking_address = '0x0000000000000000000000000000000000001010'

        amount = float(amount)
        # Get the sender's account from the private key
        sender_account = Account.from_key(private_key)

        # Check if the sender has enough balance
        sender_balance = w3.eth.get_balance(sender_account.address)
        sender_balance = float(sender_balance)
        amount_wei = w3.to_wei(amount, 'ether')
        if sender_balance < amount_wei:
            return f"Insufficient balance."

        # Get the current nonce for the sender's address
        nonce = w3.eth.get_transaction_count(sender_account.address)
        url = "https://api.polygonscan.com/api"
        params = {
            "module": "contract",
            "action": "getabi",
            "address": staking_address,
            "apikey": polyscan
        }

        response = requests.get(url, params=params)
        data = response.json()
        if data["status"] == "1":

            staking_contract = w3.eth.contract(
                address=staking_address, abi=data['result'])

            # Prepare the transaction
            tx_data = staking_contract.functions.stake().buildTransaction({
                'from': sender_account.address,
                'nonce': nonce,
                'value': amount_wei,
                'gas': 100000,
                'gasPrice': w3.eth.gas_price,
            })

            # Sign the transaction
            signed_tx = w3.eth.account.sign_transaction(tx_data, private_key)

            # Send the transaction
            tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

            return f"Staking {amount} Matic. Transaction hash: {tx_hash.hex()}"
