import time
import re
import subprocess
import json
import os

LOG_FILE = "/var/log/auth.log"
STATS_FILE = "stats.json"
FAILED_PATTERN = r"Failed password for .* from ([\d\.]+) port"
THRESHOLD = 3

# تهيئة ملف الإحصائيات
if not os.path.exists(STATS_FILE):
    with open(STATS_FILE, "w") as f:
        json.dump({"total_attempts": 0, "blocked_ips": []}, f)

attackers_db = {}

def update_stats_file(ip, is_blocked):
    try:
        with open(STATS_FILE, "r") as f:
            data = json.load(f)
        
        data["total_attempts"] += 1
        if is_blocked and ip not in data["blocked_ips"]:
            data["blocked_ips"].append(ip)
            
        with open(STATS_FILE, "w") as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Error updating stats: {e}")

def block_ip(ip):
    print(f"[!!!] ACTION: Blocking {ip}...")
    try:
        subprocess.run(f"sudo iptables -A INPUT -s {ip} -j DROP", shell=True, check=True)
        return True
    except:
        return False

def run_soar():
    print("[+] SOAR Lite Engine started...")
    with open(LOG_FILE, "r") as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            
            match = re.search(FAILED_PATTERN, line)
            if match:
                ip = match.group(1)
                attackers_db[ip] = attackers_db.get(ip, 0) + 1
                
                is_blocked = False
                if attackers_db[ip] >= THRESHOLD:
                    is_blocked = block_ip(ip)
                    attackers_db[ip] = 0 # Reset counter after block
                
                update_stats_file(ip, is_blocked)
                print(f"[!] Attempt detected from {ip}. Total for this IP: {attackers_db.get(ip, 0)}")

if __name__ == "__main__":
    run_soar()