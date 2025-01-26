import requests
from buyer_analysis import analyze_buyers, sort_by_buyers, save_buyer_data

# Base URL for API
DEX_API_URL = "https://api.dexscreener.com/token-profiles/latest/v1"

def fetch_tokens(api_url):
    """
    Fetches the latest tokens from the DEX API.
    Args:
        api_url (str): The API URL to fetch tokens from.
    Returns:
        list: A list of tokens in JSON format, or None if the request fails.
    """
    try:
        print("Fetching the latest tokens...")
        response = requests.get("https://api.dexscreener.com/token-profiles/latest/v1")
        if response.status_code == 200:
            data = response.json()  # Assuming the API returns JSON
            print("Tokens fetched successfully!")
            return data
        else:
            print(f"Failed to fetch tokens. Status Code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching tokens: {e}")
        return None

def main():
    """
    Main function to fetch, process, and save token data.
    """
    tokens = fetch_tokens(DEX_API_URL)
    if tokens and isinstance(tokens, list):  # Ensure the data is a list
        print("Analyzing buyer data...")
        buyer_data = analyze_buyers(tokens)

        if buyer_data:
            print("Sorting buyer data by number of buyers...")
            sorted_buyer_data = sort_by_buyers(buyer_data)

            print("Saving the sorted buyer data to 'buyer_data.json'...")
            save_buyer_data("buyer_data.json", sorted_buyer_data)

            print("Process complete. Buyer data saved successfully!")
        else:
            print("No meaningful buyer data found to process.")
    else:
        print("No tokens found or unable to fetch data.")

if __name__ == "__main__":
    main()
