# phishsnare-cl
# 🛡️ PhishSnare - CLI Phishing Link Detector

PhishSnare is a lightweight, command-line tool written in Python that detects suspicious or phishing URLs based on keyword patterns, IP-based URLs, and common red flags. Designed for ethical hackers, penetration testers, and cybersecurity learners — especially in Kali Linux.

---

## 🚀 Features

- Detects common phishing patterns:
  - Phishing keywords (`login`, `verify`, `paypal`, `account`, etc.)
  - IP-based URLs (e.g., `http://192.168.x.x`)
  - Suspicious characters like `@` or `--`
- Simple and fast CLI interface
- No internet required — runs fully offline
- Works on Kali Linux, Ubuntu, ParrotOS, etc.

---

## 🎯 How to Use

### ▶️ Run directly with Python:
```bash
python3 phishsnare.py https://login-update-paypal.ru

██████╗ ██╗  ██╗██╗███████╗██╗  ██╗███████╗███╗   ██╗██╗   ██╗███████╗
██╔══██╗██║  ██║██║██╔════╝██║  ██║██╔════╝████╗  ██║██║   ██║██╔════╝
██████╔╝███████║██║███████╗███████║█████╗  ██╔██╗ ██║██║   ██║█████╗  
██╔═══╝ ██╔══██║██║╚════██║██╔══██║██╔══╝  ██║╚██╗██║██║   ██║██╔══╝  
██║     ██║  ██║██║███████║██║  ██║███████╗██║ ╚████║╚██████╔╝███████╗
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝

        🛡️  PhishSnare - Phishing Link Detector (CLI Edition)

[~] Analyzing URL: https://login-update-paypal.ru

[!] Result:
⚠️  Potential Phishing Link Detected!
   - Keyword matched: 'login'
   - Keyword matched: 'paypal'
----------------------------------------------------------------------------------------------------------------------------------------------------------------



🛠️ Installation (Optional)
To run it from anywhere as phishsnare:
chmod +x install.sh
./install.sh
Then:
phishsnare https://example.com
