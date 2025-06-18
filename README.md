# Relq Cybersecurity Course – Python Security Tools

This repository contains Python-based security tools and scripts developed as part of the **Relq** cybersecurity course. Each script demonstrates a key concept or technique used in ethical hacking, penetration testing, or system hardening.

---

## 📁 Topics Covered

This course focuses on practical, offensive security tasks written in Python:

1. **Network Scanner** – Discover live hosts and open ports in a network.
2. **Directory Enumeration** – Enumerate hidden directories on web servers.
3. **Subdomain Discovery** – Identify subdomains of a target domain.
4. **SSH Brute Force Tool** – Attempt SSH login using a dictionary attack (for testing in a lab only).
5. **Hash Identifier** – Analyze a given hash and guess the hashing algorithm.
6. **Hash Cracker** – Crack common password hashes using wordlists.
7. **Log Analyzer** – Parse system or web logs to extract security-relevant information.

---

## 🛠 Tools & Technologies

- Python 3.x
- `socket`, `os`, `requests`, `paramiko`, `hashlib`, and other standard libraries
- Linux (Kali, Ubuntu, etc.)
- Git / GitHub

---

# Network scanner
python3 network_scanner.py 192.168.1.1 --start-port 20 --end-port 100

# Directory enumerator
python3 directory_enum.py http://example.com wordlist.txt --threads 10

# Subdomain Enumeration
python3 subdomain_discovery.py example.com subs.txt --threads 20

# SSH Brute Force
python3 ssh_bruteforce.py --host 192.168.1.100 --port 22 --users users.txt --passwords passwords.txt --threads 10

# Hash Identifier
python3 hash_identifier.py --hash "5f4dcc3b5aa765d61d8327deb882cf99"

# Hash Cracker
python3 hash_cracker.py --hash <hash> --type md5 --wordlist words.txt
