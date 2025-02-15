# Solana Token Purchase Tracker (Under Development) --
The Project is still under developement 
# Ensure JSON and Environment is Installed perfectly 

# Overview
This project is designed to track and analyze the purchase behavior of Solana token buyers, specifically focusing on identifying new accounts that have just made their first Solana token purchase. The goal is to spot these new buyers and check for any excess Solana in their account, which may indicate their likelihood of purchasing more tokens in the future. This information can be useful for tracking the early adoption of newly launched tokens on the Solana blockchain.

# Key Features
First Purchase Detection: Identifies accounts that have made their first Solana token purchase.
Extra Solana Detection: Tracks accounts with extra Solana in their wallet, suggesting potential for future token purchases.
Focus on Solana Tokens: This model is specifically focused on Solana-based tokens, utilizing the Solana blockchain's unique attributes.
DEX Screener Integration: Uses data from decentralized exchange (DEX) platforms that support the Solana blockchain to identify tokens and their buyers.
New Token Launches: Tracks newly launched Solana tokens to identify potential early adopters.

# Purpose
The goal of this project is to create a model that:

Detects the first purchase: It monitors Solana transactions to pinpoint the accounts that are making their very first purchase of a token.
Tracks Solana balance: After a first purchase is detected, the model analyzes whether the account holds extra Solana tokens (beyond what was spent) that may indicate the possibility of future token purchases.
Helps identify early buyers: This model provides insights into potential early adopters of new tokens, which can be valuable for token projects, investors, and analysts interested in Solana's ecosystem.

# Technologies Used
Solana Blockchain: The project leverages the Solana blockchain for transaction tracking.
DEX Screener API: Uses DEX screener platforms that support Solana tokens to access real-time trading data.
Python: Python is used for the data collection, processing, and analysis tasks.
Web Scraping/Blockchain Monitoring: Integrates with APIs or web scraping methods to collect transaction data from decentralized exchanges.


# Download the Repository  
https://github.com/shnav3105/Solana.git

Setup
1. Create a Virtual Environment
To set up the project environment, create a virtual environment:

`python -m venv venv`


2. Install Required Libraries
Install the necessary libraries for the project:

`pip install requests pandas solana`


3. DEX Screener API
The project uses the DEX Screener API to fetch token profiles. The API URL is:

`DEX_API_URL = Available in Dex Screener Api Reference`


4. Run Command
` python solana.py`


# solana_wallet_analysis
1. solana wallet analysis file structure
   
solana_wallet_analysis/
|
├── main.py          
├── solana_utils.py  
├── config.py        
└── __init__.py       

2. Install Required Libraries
   `pip install solana`
   
3. Get you Alchemy RPC API KEY for config.py
4. Have Your Wallet Address
5. Run command `python main.py`

