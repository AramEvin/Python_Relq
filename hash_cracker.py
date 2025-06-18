import hashlib
import argparse
import sys

def crack_hash(target_hash, hash_type, wordlist_path):
    hash_type = hash_type.lower()
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                password = line.strip()
                if not password:
                    continue

                # Convert password to hash using the chosen algorithm
                try:
                    hash_func = getattr(hashlib, hash_type)
                except AttributeError:
                    print(f"[-] Unsupported hash type: {hash_type}")
                    return

                result = hash_func(password.encode()).hexdigest()
                if result == target_hash.lower():
                    print(f"[+] Password found: {password}")
                    return
        print("[-] Password not found in the wordlist.")
    except FileNotFoundError:
        print("[-] Wordlist file not found.")
    except Exception as e:
        print(f"[!] Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Hash Cracker Tool")
    parser.add_argument("--hash", required=True, help="The hash to crack")
    parser.add_argument("--type", required=True, help="Hash type (md5, sha1, sha256, etc.)")
    parser.add_argument("--wordlist", required=True, help="Path to password wordlist")
    args = parser.parse_args()

    print(f"\n[*] Starting hash cracking (type: {args.type.upper()})...")
    crack_hash(args.hash, args.type, args.wordlist)

if __name__ == "__main__":
    main()
