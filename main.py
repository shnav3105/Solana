from solana_utils import analyze_wallet, save_to_file
from config import WALLET_ADDRESS

if __name__ == "__main__":
    print(f"Analyzing wallet: {WALLET_ADDRESS}")
    wallet_data = analyze_wallet(WALLET_ADDRESS)

    # Display balance
    print(f"Wallet Balance: {wallet_data['balance']} SOL")
    
    # Display transactions
    print(f"Found {len(wallet_data['transactions'])} transactions")
    for tx in wallet_data["transactions"]:
        print(f"Signature: {tx['signature']}, Slot: {tx['slot']}")

    # Save to file
    save_to_file(wallet_data)
