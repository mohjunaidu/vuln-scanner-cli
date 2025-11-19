import requests
from colorama import Fore, Style

def check_headers(url):
    print(Fore.CYAN + "\n[+] Checking Security Headers" + Style.RESET_ALL)

    missing_headers = []
    
    try:
        res = requests.get(url, timeout=10)
        headers = res.headers
    except:
        print(Fore.RED + "Failed to load URL." + Style.RESET_ALL)
        return {"missing_headers": []}

    required = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-XSS-Protection",
        "Strict-Transport-Security",
        "X-Content-Type-Options",
        "Referrer-Policy"
    ]

    for header in required:
        if header in headers:
            print(Fore.GREEN + f"✓ {header}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"x {header} missing" + Style.RESET_ALL)
            missing_headers.append(header)
    
    return {"missing_headers": missing_headers}

