import time
import re

# مسار ملف السجلات في أوبونتو
LOG_FILE = "/var/log/auth.log"

# النمط الذي نبحث عنه (محاولة فاشلة)
# مثال للسطر: Apr 10 00:00:00 workmachine sshd[123]: Failed password for root from 192.168.1.1 port 1234 ssh2
FAILED_PATTERN = r"Failed password for .* from ([\d\.]+) port"

def watch_logs():
    print("[+] SOAR Lite: Starting Log Watcher...")
    
    # فتح الملف وقراءة الأسطر الجديدة فقط
    with open(LOG_FILE, "r") as f:
        # الذهاب إلى آخر الملف
        f.seek(0, 2)
        
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)  # انتظار سطر جديد
                continue
            
            # البحث عن النمط
            match = re.search(FAILED_PATTERN, line)
            if match:
                attacker_ip = match.group(1)
                print(f"[!] ALERT: Failed login attempt detected from IP: {attacker_ip}")
                # هنا سنضيف لاحقاً وظيفة الاستجابة (The Response)

if __name__ == "__main__":
    try:
        watch_logs()
    except KeyboardInterrupt:
        print("\n[+] Stopping SOAR...")