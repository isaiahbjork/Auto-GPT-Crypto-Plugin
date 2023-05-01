import os
from web3 import Web3, HTTPProvider
from eth_account import Account
from web3.contract import Contract
Account.enable_unaudited_hdwallet_features()
address = os.getenv('ETH_WALLET_ADDRESS')
private_key = os.getenv('ETH_WALLET_PRIVATE_KEY')


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

    def stake_matic(amount, private_key, endpoint):
        w3 = Web3(Web3.HTTPProvider(f'{endpoint}/polygon'))
        staking_address = '0x5e3Ef299fDDf15eAa0432E6e66473ace8c13D908'

        # Get the sender's account from the private key
        sender_account = Account.from_key(private_key)

        # Check if the sender has enough balance
        sender_balance = w3.eth.get_balance(sender_account.address)
        amount_wei = w3.toWei(amount, 'ether')
        if sender_balance < amount_wei:
            return f"Insufficient balance."

        # Get the current nonce for the sender's address
        nonce = w3.eth.get_transaction_count(sender_account.address)
        # Get the ANIToken contract instance
        contract = w3.eth.contract(address=staking_address)

        # Get the contract ABI
        abi = contract.abi
        # Instantiate the staking contract
        staking_contract = Contract.from_abi('Staking', staking_address, abi)

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

        return f"Staking Matic. Transaction hash: {tx_hash.hex()}"
