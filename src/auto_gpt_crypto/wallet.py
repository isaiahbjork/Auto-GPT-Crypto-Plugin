from web3 import Web3, HTTPProvider
from eth_account import Account
Account.enable_unaudited_hdwallet_features()

class Wallet():

    def send_eth(recipient_address, private_key, amount, endpoint):
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