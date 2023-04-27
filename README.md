# Auto-GPT Crypto Plugin 📈

⚠️ WARNING: NOT 100% COMPLETE

The AutoGPT Crypto Plugin is a software tool that enables traders to connect their Crypto wallet or exchange to Auto-GPT.


[![GitHub Repo stars](https://img.shields.io/github/stars/isaiahbjork/Auto-GPT-Crypto-Plugin?style=social)](https://github.com/isaiahbjork/Auto-GPT-Crypto-Plugin/stargazers)

## 💡 Key Features:

- **Get ETH Balance**
- **Get Wallet Token Holdings** (ETH, BSC, Fantom, Avalanche, Polygon, Arbitrum, Syscoin, Optimism)
- **Get Wallet NFT Holdings**
- **Get Coin/NFT of The Day**
- **Buy ERC-20 Tokens** (In-Progress)
- **Swap Tokens**  (In-Progress)
- **Search Top Holders**  (In-Progress)
- **Stake Tokens** (In-Progress)
- **Send Tokens**  (In-Progress)
- **Get Coins By Market Cap**  (In-Progress)
- **Get New Tokens**  (In-Progress)
- **Trade on Exchanges**  (In-Progress)

## 🔧 Installation

Follow these steps to configure the Auto-GPT Crypto Plugin:

### 1. Clone the Auto-GPT-Crypto-Plugin repository

Clone this repository and navigate to the `Auto-GPT-Crypto-Plugin` folder in your terminal:

```bash
git clone https://github.com/isaiahbjork/Auto-GPT-Crypto-Plugin.git
```

### 2. Install required dependencies

Execute the following command to install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 3. Package the plugin as a Zip file

Compress the `Auto-GPT-Crypto-Plugin` folder or [download the repository as a zip file](https://github.com/isaiahbjork/Auto-GPT-Crypto-Plugin/archive/refs/heads/master.zip).

### 4. Install Auto-GPT

If you haven't already, clone the [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) repository, follow its installation instructions, and navigate to the `Auto-GPT` folder.

You might have to run this in the Auto-GPT file if you get an error saying "No Moudle Found".

```bash
pip install web3 eth-account ccxt
```

### 5. Copy the Zip file into the Auto-GPT Plugin folder

Transfer the zip file from step 3 into the `plugins` subfolder within the `Auto-GPT` repo.

### 6. Locate the `.env.template` file

Find the file named `.env.template` in the main `/Auto-GPT` folder.

### 7. Create and rename a copy of the file

Duplicate the `.env.template` file and rename the copy to `.env` inside the `/Auto-GPT` folder.

### 8. Edit the `.env` file

Open the `.env` file in a text editor. Note: Files starting with a dot might be hidden by your operating system.

### 9. Add Crypto configuration settings

Append the following configuration settings to the end of the file:

```ini
################################################################################
### CRYPTO
################################################################################
INFURA_API_KEY=
ETHERSCAN_API_KEY=
ETH_WALLET_ADDRESS=
ETH_WALLET_PRIVATE_KEY=
ETH_NETWORK=
LUNAR_CRUSH_API_KEY=
### Exchanges
EXCHANGES=
KRAKEN_API_KEY=
KRAKEN_SECRET=
COINBASE_API_KEY=
COINBASE_SECRET=
```

- Create a [Infura](https://infura.io) account.
- Create a [Etherscan](https://etherscan.io) account.
- Create a [LunarCrush](https://lunarcrush.com) account.
- Set `INFURA_API_KEY` to your Infura account ID.
- Set `ETHERSCAN_API_KEY` to your Etherscan API Key.
- Set `LUNAR_CRUSH_API_KEY` to your LunarCrush API Key.
- Set `ETH_WALLET_ADDRESS` to your Ethereum Wallet Address.
- Set `ETH_WALLET_PRIVATE_KEY` to your Ethereum mnemonic.
- Set `ETH_NETWORK` to your Ethereum Network (mainnet or sepolia).
- Set `EXCHANGES` to the crypto exchanges where you have an account. Review available [exchanges](/src/auto_gpt_crypto/exchanges.txt). (Example: binance,kraken,bybit)
- Set `KRAKEN_API_KEY` to your Kraken API Key.
- Set `KRAKEN_SECRET` to your Kraken Secret.

### 10. Allowlist Plugin

In your `.env` search for `ALLOWLISTED_PLUGINS` and add this Plugin:

```ini
################################################################################
### ALLOWLISTED PLUGINS
################################################################################
#ALLOWLISTED_PLUGINS - Sets the listed plugins that are allowed (Example: plugin1,plugin2,plugin3)
ALLOWLISTED_PLUGINS=AutoGPTCryptoPlugin
```

### 11. Review Available Commands
You can review the available commands [here](/src/auto_gpt_crypto/commands.txt).

## 🧪 Test the Auto-GPT Crypto Plugin

Experience the plugin's capabilities by testing it for
