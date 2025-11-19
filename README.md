# Vulnerability Scanner CLI

A lightweight command-line vulnerability scanner built with Python.  
Designed to demonstrate cybersecurity fundamentals such as reconnaissance, enumeration, security header validation, and basic misconfiguration discovery.

## 🔍 Features
- Security header analysis  
- Directory enumeration  
- Server info fingerprinting  
- Checks for exposed `.env`, `.git`, and backup files  
- Generates readable CLI output  
- Zero dependencies beyond `requests` and `colorama`

## 🚀 Quick Start
```bash
git clone https://github.com/<your-username>/vuln-scanner-cli
cd vuln-scanner-cli
pip install -r requirements.txt
python3 scanner.py https://example.com
```

## 📁 Project Structure

vuln-scanner-cli/
│── scanner.py
│── modules/
│── wordlists/
│── reports/

## ⚠️ Legal Disclaimer

This tool is for educational use only.
Do not scan websites you do not own or have permission to test.

