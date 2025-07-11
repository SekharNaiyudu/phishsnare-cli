#!/usr/bin/env python3
import re
import sys
import time
import argparse

def show_banner():
    print(r"""
██████╗ ██╗  ██╗██╗███████╗██╗  ██╗███████╗███╗   ██╗██╗   ██╗███████╗
██╔══██╗██║  ██║██║██╔════╝██║  ██║██╔════╝████╗  ██║██║   ██║██╔════╝
██████╔╝███████║██║███████╗███████║█████╗  ██╔██╗ ██║██║   ██║█████╗  
██╔═══╝ ██╔══██║██║╚════██║██╔══██║██╔══╝  ██║╚██╗██║██║   ██║██╔══╝  
██║     ██║  ██║██║███████║██║  ██║███████╗██║ ╚████║╚██████╔╝███████╗
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝

        🛡️  PhishSnare - Phishing Link Detector (CLI Edition)
    """)

def analyze_url(url):
    phishing_keywords = ['login', 'account', 'verify', 'secure', 'bank', 'paypal', 'amazon', 'ebay']
    suspicious_patterns = [
        r'^http:\/\/\d{1,3}(\.\d{1,3}){3}',
        r'@',
        r'[-]{2,}',
    ]

    print("\n[~] Analyzing URL:", url)
    time.sleep(1)

    is_phishing = False
    reasons = []

    for kw in phishing_keywords:
        if kw in url.lower():
            is_phishing = True
            reasons.append(f"Keyword matched: '{kw}'")

    for pattern in suspicious_patterns:
        if re.search(pattern, url):
            is_phishing = True
            reasons.append(f"Suspicious pattern: {pattern}")

    if 'trusted-domain.com' in url:
        is_phishing = False
        reasons = ["Trusted domain found — bypassing alerts."]

    print("\n[!] Result:")
    if is_phishing:
        print("⚠️  Potential Phishing Link Detected!")
        for r in reasons:
            print("   -", r)
    else:
        print("✅ This link seems safe (but always verify manually).")

if __name__ == '__main__':
    show_banner()
    parser = argparse.ArgumentParser(description="PhishSnare - Phishing Link Detector")
    parser.add_argument("url", help="URL to analyze (e.g., https://example.com/login)")
    args = parser.parse_args()

    if not args.url.startswith("http://") and not args.url.startswith("https://"):
        print("❌ Invalid URL format. Use http:// or https://")
        sys.exit(1)

    analyze_url(args.url)
