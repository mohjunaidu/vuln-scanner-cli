import requests
from colorama import Fore, Style

def enumerate_dirs(url):
    print(Fore.CYAN + "\n[+] Directory Enumeration" + Style.RESET_ALL)

    wordlist_path = "wordlists/small.txt"
    accessible_dirs = []

    try:
        with open(wordlist_path, "r") as f:
            dirs = f.read().splitlines()
    except:
        print(Fore.RED + "Wordlist missing." + Style.RESET_ALL)
        return {"accessible_dirs": []}

    for d in dirs:
        if not d.strip():  # Skip empty lines
            continue
        full = f"{url}/{d}"
        try:
            res = requests.get(full, timeout=5)
            if res.status_code == 200:
                print(Fore.GREEN + f"[200] {full}" + Style.RESET_ALL)
                accessible_dirs.append(full)
            elif res.status_code == 403:
                print(Fore.YELLOW + f"[403] {full}" + Style.RESET_ALL)
        except:
            pass  # Silently skip failed requests
    
    return {"accessible_dirs": accessible_dirs}

