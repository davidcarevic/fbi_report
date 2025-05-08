import requests
import json

def fetch_fbi_wanted():
    url = 'https://api.fbi.gov/wanted/v1/list'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        print("=== FBI Wanted List ===\n")
        for item in data.get('items', [])[:10]:  # Limit to first 10 results
            print(f"Title     : {item.get('title', 'N/A')}")
            print(f"Name      : {item.get('subject', 'N/A')}")
            print(f"UID       : {item.get('uid', 'N/A')}")
            print(f"Image URL : {item.get('images', [{}])[0].get('original', 'N/A')}")
            print("-" * 40)
    except requests.RequestException as e:
        print("Error fetching FBI data:", e)

if __name__ == "__main__":
    fetch_fbi_wanted()
