# directory_enum.py

import requests
import argparse
from concurrent.futures import ThreadPoolExecutor

def check_directory(url, directory):
    full_url = f"{url.rstrip('/')}/{directory.strip()}"
    try:
        response = requests.get(full_url, timeout=3)
        if response.status_code in [200, 301, 302]:
            print(f"[+] Found: {full_url} (Status: {response.status_code})")
    except requests.RequestException:
        pass  # Ignore failed requests

def main():
    parser = argparse.ArgumentParser(description="Directory Enumeration Tool")
    parser.add_argument("url", help="Target base URL (e.g. http://example.com)")
    parser.add_argument("wordlist", help="Path to wordlist file")
    parser.add_argument("--threads", type=int, default=10, help="Number of threads (default: 10)")
    args = parser.parse_args()

    try:
        with open(args.wordlist, "r") as file:
            directories = file.read().splitlines()
    except FileNotFoundError:
        print("[-] Wordlist file not found.")
        return

    print(f"\n[*] Starting directory enumeration on: {args.url}")
    print(f"[*] Using {args.threads} threads\n")

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        for directory in directories:
            executor.submit(check_directory, args.url, directory)

if __name__ == "__main__":
    main()
