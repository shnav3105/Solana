# Solana Token Purchase Tracker (Under Development)
The Project is still under developement 

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
