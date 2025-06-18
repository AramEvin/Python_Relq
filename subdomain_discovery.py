# subdomain_discovery.py

import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def resolve_subdomain(domain, subdomain):
    full_domain = f"{subdomain.strip()}.{domain}"
    try:
        ip = socket.gethostbyname(full_domain)
        print(f"[+] Found: {full_domain} -> {ip}")
    except socket.gaierror:
        pass  # Ignore subdomains that don't resolve

def main():
    parser = argparse.ArgumentParser(description="Subdomain Discovery Tool")
    parser.add_argument("domain", help="Target domain (e.g. example.com)")
    parser.add_argument("wordlist", help="Wordlist file with subdomain prefixes")
    parser.add_argument("--threads", type=int, default=10, help="Number of threads (default: 10)")
    args = parser.parse_args()

    try:
        with open(args.wordlist, "r") as file:
            subdomains = file.read().splitlines()
    except FileNotFoundError:
        print("[-] Wordlist file not found.")
        return

    print(f"\n[*] Starting subdomain enumeration for: {args.domain}")
    print(f"[*] Using {args.threads} threads\n")

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        for sub in subdomains:
            executor.submit(resolve_subdomain, args.domain, sub)

if __name__ == "__main__":
    main()
