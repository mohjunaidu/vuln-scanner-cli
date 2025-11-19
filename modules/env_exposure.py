import requests
from colorama import Fore, Style

def check_env_files(url):
    print(Fore.CYAN + "\n[+] Checking for Exposed Environment Files" + Style.RESET_ALL)

    sensitive = [".env", ".git/", "backup.zip", "db.sql"]
    exposed_files = []

    for path in sensitive:
        full = f"{url}/{path}"
        try:
            res = requests.get(full, timeout=5)
            if res.status_code == 200:
                print(Fore.RED + f"EXPOSED: {full}" + Style.RESET_ALL)
                exposed_files.append(full)
        except:
            pass  # Silently skip failed requests
    
    return {"exposed_files": exposed_files}

