# Auto-GPT Crypto Plugin 📈

The AutoGPT Crypto Plugin is a software tool that enables traders to connect their Crypto wallet or exchange to Auto-GPT.

[![GitHub Repo stars](https://img.shields.io/github/stars/isaiahbjork/Auto-GPT-Crypto-Plugin?style=social)](https://github.com/isaiahbjork/Auto-GPT-Crypto-Plugin/stargazers)

## 💡 Key Features:

- **Get ETH Balance**
- **Buy ERC-20 Tokens**
- **Swap Tokens**
- **Search Top Holders**
- **Get Wallet Token Holdings**
- **Stake Tokens**
- **Send Tokens**
- **Get Coins By Market Cap**
- **Get New Tokens**
- **Trade on Exchanges**

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
pip install web3 eth-abi
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
```

- Create a [Infura](https://infuro.io) account.
- Create a [Etherscan](https://etherscan.io) account.
- Set `INFURA_API_KEY` to your Infura account ID.
- Set `ETHERSCAN_API_KEY` to your Etherscan API Key.
- Set `ETH_WALLET_ADDRESS` to your Ethereum Wallet Address.
- Set `ETH_WALLET_PRIVATE_KEY` to your Ethereum Private Key.

### 10. Allowlist Plugin

In your `.env` search for `ALLOWLISTED_PLUGINS` and add this Plugin:

```ini
################################################################################
### ALLOWLISTED PLUGINS
################################################################################
#ALLOWLISTED_PLUGINS - Sets the listed plugins that are allowed (Example: plugin1,plugin2,plugin3)
ALLOWLISTED_PLUGINS=AutoGPTCryptoPlugin
```

## 🧪 Test the Auto-GPT Crypto Plugin

Experience the plugin's capabilities by testing it for
