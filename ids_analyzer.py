import re
from collections import defaultdict

failed_attempts = defaultdict(int)

log_file = input("Enter log file name: ")

try:
    with open(log_file, "r") as file:

        for line in file:

            if "Failed password" in line:

                ip_match = re.search(r"\d+\.\d+\.\d+\.\d+", line)

                if ip_match:

                    ip = ip_match.group()

                    failed_attempts[ip] += 1

    print("\n===== Intrusion Detection Report =====\n")

    for ip, count in failed_attempts.items():

        if count >= 5:

            print(f"🚨 ALERT: Possible brute-force attack from {ip} ({count} attempts)")

        elif count >= 3:

            print(f"⚠️ Suspicious activity from {ip} ({count} attempts)")

except FileNotFoundError:

    print("Log file not found.")
