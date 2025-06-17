#python3 network_scanner.py 192.168.1.1 --start-port 20 --end-port 65000

import socket
import argparse

def scan_target(ip, port):
    """
    Try to connect to a port on the given IP address.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # short timeout
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()
    except socket.error:
        print(f"[-] Cannot connect to {ip}")
        return

def main():
    parser = argparse.ArgumentParser(description="Simple Python Network Port Scanner")
    parser.add_argument("target", help="Target IP address (e.g., 192.168.1.1)")
    parser.add_argument("--start-port", type=int, default=1, help="Start of port range (default: 1)")
    parser.add_argument("--end-port", type=int, default=1024, help="End of port range (default: 1024)")
    args = parser.parse_args()

    print(f"\n[*] Scanning target {args.target} from port {args.start_port} to {args.end_port}\n")

    for port in range(args.start_port, args.end_port + 1):
        scan_target(args.target, port)

if __name__ == "__main__":
    main()
