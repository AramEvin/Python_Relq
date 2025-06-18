import re
import argparse

SUSPICIOUS_WORDS = ['verify', 'login', 'account', 'urgent', 'update', 'click here']
LOOKALIKE_DOMAINS = ['g00gle.com', 'paypai.com', 'micros0ft.com', 'faceb00k.com']

def extract_links(content):
    return re.findall(r'https?://[^\s"\'>]+', content)

def check_for_indicators(email_text):
    indicators = {
        "links": [],
        "suspicious_words": [],
        "lookalike_domains": [],
    }

    # Links
    links = extract_links(email_text)
    indicators["links"] = links

    # Suspicious Words
    for word in SUSPICIOUS_WORDS:
        if word in email_text.lower():
            indicators["suspicious_words"].append(word)

    # Lookalike Domains
    for domain in LOOKALIKE_DOMAINS:
        if domain in email_text.lower():
            indicators["lookalike_domains"].append(domain)

    return indicators

def main():
    parser = argparse.ArgumentParser(description="Email Phishing Detector")
    parser.add_argument('--email', required=True, help='Path to .eml or text email')
    args = parser.parse_args()

    try:
        with open(args.email, 'r', encoding='utf-8', errors='ignore') as f:
            email_text = f.read()
    except FileNotFoundError:
        print("[-] Email file not found.")
        return

    print("[*] Analyzing email...")
    indicators = check_for_indicators(email_text)

    print("\n=== Results ===")
    if indicators["links"]:
        print("[+] Found Links:")
        for link in indicators["links"]:
            print(f"   - {link}")
    if indicators["suspicious_words"]:
        print("[!] Suspicious Words:")
        print("   ", ", ".join(indicators["suspicious_words"]))
    if indicators["lookalike_domains"]:
        print("[!] Lookalike Domains:")
        print("   ", ", ".join(indicators["lookalike_domains"]))
    if not any(indicators.values()):
        print("[+] No obvious phishing indicators found.")

if __name__ == "__main__":
    main()
