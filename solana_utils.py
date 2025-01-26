import requests
import json
from config import ALCHEMY_RPC_URL

def fetch_wallet_balance(wallet_address):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBalance",
        "params": [wallet_address]
    }
    response = requests.post(ALCHEMY_RPC_URL, json=payload).json()
    balance = response["result"]["value"] / 1e9  # Convert lamports to SOL
    return balance

def fetch_transaction_history(wallet_address, limit=10):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getSignaturesForAddress",
        "params": [wallet_address, {"limit": limit}]
    }
    response = requests.post(ALCHEMY_RPC_URL, json=payload).json()
    transactions = response["result"]
    return transactions

def analyze_wallet(wallet_address):
    balance = fetch_wallet_balance(wallet_address)
    transactions = fetch_transaction_history(wallet_address)
    return {
        "wallet_address": wallet_address,
        "balance": balance,
        "transactions": transactions,
    }

def save_to_file(data, filename="wallet_analysis.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filename}")
