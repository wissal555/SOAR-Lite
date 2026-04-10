# 🛡️ SOAR Lite: Automated Threat Response System

A Python-based Security Orchestration, Automation, and Response (SOAR) tool that monitors system logs, detects brute-force attacks, and automatically blocks attackers using Linux iptables.

## ✨ Features
- **Real-time Monitoring:** Watches `/var/log/auth.log` for failed SSH attempts.
- **Automated Response:** Automatically drops IP addresses after 3 failed attempts.
- **Interactive Dashboard:** Built with Flask and JavaScript to display live statistics.
- **Persistent Logging:** Tracks total attacks and currently blocked IPs.

## 🚀 Tech Stack
- **Backend:** Python (Regex, Subprocess)
- **Web Server:** Flask
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
- **Security:** Linux iptables, UFW


