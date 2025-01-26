import json

# analyze_buyers(data): Extract meaningful data from the input
def analyze_buyers(data):
    buyer_data = []
    for token in data:
        # Extract buyers, sellers, and transactions with default values
        buyers = token.get("buyVolume", 0)
        sellers = token.get("sellVolume", 0)
        transaction_count = token.get("txns", {}).get("total", 0)

        # Add meaningful tokens to the list if buyers > 0
        buyer_data.append({
            "name": token.get("name", "Unknown"),
            "address": token.get("address", None),
            "chain": token.get("chainId", "Unknown"),
            "buyers": buyers,
            "sellers": sellers,
            "transactions": transaction_count
        })

    return buyer_data


# Sort the buyer data by the number of buyers in descending order
def sort_by_buyers(buyer_data):
    return sorted(buyer_data, key=lambda x: x["buyers"], reverse=True)


# Save the buyer data to a JSON file
def save_buyer_data(filename, buyer_data):
    try:
        with open(filename, "w") as file:
            json.dump(buyer_data, file, indent=4)
        print(f"Buyer data saved successfully to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")
