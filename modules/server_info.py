import requests
from colorama import Fore, Style

def check_server(url):
    print(Fore.CYAN + "[+] Fingerprinting Server" + Style.RESET_ALL)

    try:
        res = requests.get(url, timeout=10)
        server = res.headers.get("Server", "Not disclosed")
        print(Fore.YELLOW + f"Server: {server}" + Style.RESET_ALL)
        return {"server_disclosed": server}
    except:
        print(Fore.RED + "Could not fingerprint server." + Style.RESET_ALL)
        return {"server_disclosed": "Not disclosed"}

