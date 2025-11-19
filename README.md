# Vulnerability Scanner CLI

A lightweight command-line vulnerability scanner built with Python.  
Designed to demonstrate cybersecurity fundamentals such as reconnaissance, enumeration, security header validation, and basic misconfiguration discovery.

##  Features
- Security header analysis  
- Directory enumeration  
- Server info fingerprinting  
- Checks for exposed `.env`, `.git`, and backup files  
- **Automated fix suggestions** with implementation examples
- Generates readable CLI output with color-coded results
- Zero dependencies beyond `requests` and `colorama`

##  Quick Start
```bash
git clone https://github.com/mohjunaidu/vuln-scanner-cli
cd vuln-scanner-cli
pip install -r requirements.txt
python3 scanner.py https://example.com
```

##  Fix Suggestions

After scanning, the tool automatically provides actionable fix suggestions for each vulnerability found:
- **Missing Security Headers**: Example configurations for Apache, Nginx, Express.js, and Django
- **Server Information Disclosure**: Steps to hide server headers
- **Exposed Files**: Immediate actions to secure sensitive files
- **Accessible Directories**: Recommendations for access control

Each suggestion includes:
- Purpose and explanation
- Example configuration
- Platform-specific implementation steps

##  Project Structure

vuln-scanner-cli/
│── scanner.py
│── modules/
│── wordlists/
│── reports/

##  Legal Disclaimer

This tool is for educational use only.
Do not scan websites you do not own or have permission to test.

