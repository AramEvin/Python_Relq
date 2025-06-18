import argparse
import re

def identify_hash(hash_str):
    hash_str = hash_str.strip().lower()

    patterns = {
        "MD5": r"^[a-f0-9]{32}$",
        "SHA-1": r"^[a-f0-9]{40}$",
        "SHA-224": r"^[a-f0-9]{56}$",
        "SHA-256": r"^[a-f0-9]{64}$",
        "SHA-384": r"^[a-f0-9]{96}$",
        "SHA-512": r"^[a-f0-9]{128}$",
        "NTLM": r"^[a-f0-9]{32}$",
        "MySQL 5.x": r"^[a-f0-9]{40}$",
        "bcrypt": r"^\$2[abxy]?\$\d{2}\$[./A-Za-z0-9]{53}$",
        "DES(Unix)": r"^.{13}$",
        "Base64": r"^[A-Za-z0-9+/=]{16,}$"
    }

    matches = []

    for hash_type, pattern in patterns.items():
        if re.fullmatch(pattern, hash_str):
            matches.append(hash_type)

    return matches if matches else ["Unknown"]

def main():
    parser = argparse.ArgumentParser(description="Hash Identifier Tool")
    parser.add_argument("--hash", required=True, help="Hash string to identify")
    args = parser.parse_args()

    print(f"\n[*] Identifying hash: {args.hash}")
    result = identify_hash(args.hash)
    print("[+] Possible types:")
    for match in result:
        print(f"    - {match}")

if __name__ == "__main__":
    main()
