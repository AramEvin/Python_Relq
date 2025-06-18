import argparse
import re
from collections import Counter

def parse_log_line(line):
    # Regex for common Apache log format
    log_pattern = r'^(\S+) \S+ \S+ \[.*?\] "(.*?)" (\d{3}) \d+ ".*?" "(.*?)"$'
    match = re.match(log_pattern, line)
    if match:
        ip = match.group(1)
        request = match.group(2)
        status = match.group(3)
        agent = match.group(4)
        method = request.split()[0] if request else "-"
        return ip, method, status, agent
    return None, None, None, None

def analyze_log(file_path):
    ip_counter = Counter()
    status_counter = Counter()
    method_counter = Counter()
    error_ips = Counter()

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                ip, method, status, agent = parse_log_line(line)
                if ip:
                    ip_counter[ip] += 1
                    status_counter[status] += 1
                    method_counter[method] += 1
                    if status.startswith("4") or status.startswith("5"):
                        error_ips[ip] += 1
    except FileNotFoundError:
        print("[-] Log file not found.")
        return

    print("\n=== Top 5 IPs ===")
    for ip, count in ip_counter.most_common(5):
        print(f"{ip}: {count} requests")

    print("\n=== HTTP Status Codes ===")
    for code, count in status_counter.items():
        print(f"{code}: {count}")

    print("\n=== Request Methods ===")
    for method, count in method_counter.items():
        print(f"{method}: {count}")

    print("\n=== Suspicious IPs (Frequent Errors) ===")
    for ip, count in error_ips.most_common(5):
        if count >= 5:
            print(f"{ip}: {count} errors")

def main():
    parser = argparse.ArgumentParser(description="Log Analyzer Tool")
    parser.add_argument("--logfile", required=True, help="Path to access log file")
    args = parser.parse_args()

    print("[*] Analyzing logs...")
    analyze_log(args.logfile)

if __name__ == "__main__":
    main()
