#!/bin/python

# Author Hackachusetts
# This program uses the "haveibeenpwned API" in order to search multiple emails for data leaks.

from getpass import getpass
import requests
import time
import sys

print('''

 ____  ____  _____    _    ____ _   _ _____ ____  
| __ )|  _ \| ____|  / \  / ___| | | | ____|  _ \ 
|  _ \| |_) |  _|   / _ \| |   | |_| |  _| | |_) |
| |_) |  _ <| |___ / ___ \ |___|  _  | |___|  _ < 
|____/|_| \_\_____/_/   \_\____|_| |_|_____|_| \_|

''')

print("Breacher version 1.0\nAuthor: Hackachusetts")
print("This program uses the 'haveibeenpwned API' in order to search multiple emails for data leaks.")
print("The author is not responsible illegal actvity or misuse of this tool. Use wisely.")
print("With great power comes great responsibilty.\n")

API_KEY = getpass("Enter your api key:\n")

NUM_OF_ACCOUNTS = int(input("Enter the number of emails you'd like to search (max = 10)\n"))
accounts = list()

if num_of_accounts > 10:
    print("Number of accounts exceeds limit. Goodbye")
    sys.exit()

for email in range(num_of_accounts):
    email = input("Enter email:")
    accounts.append(email)

for account in accounts:
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{account}"

    headers = {
        "hibp-api-key": API_KEY
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        
        if not data:
            print("Empty response.")
        else:
            for names in data:
                names.get("Names")
                print(f"[+] {account} was found in the following breaches: {names}")

        time.sleep(20)

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"[+] {account} has not been found in any data breaches.")
        else:
            print(f"HTTP error: {http_err}")
            print(response.text)
    
    except requests.exceptions.RequestException as req_err:
        print(f"Request err: {req_err}")
