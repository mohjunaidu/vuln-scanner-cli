import sys
from modules.headers import check_headers
from modules.server_info import check_server
from modules.directory_enum import enumerate_dirs
from modules.env_exposure import check_env_files
from modules.suggestions import print_suggestions

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scanner.py <url>")
        return

    url = sys.argv[1]

    print("\n=== Vulnerability Scanner CLI ===\n")
    
    # Run scans and collect findings
    findings = {}
    
    server_result = check_server(url)
    if server_result:
        findings.update(server_result)
    
    headers_result = check_headers(url)
    if headers_result:
        findings.update(headers_result)
    
    dirs_result = enumerate_dirs(url)
    if dirs_result:
        findings.update(dirs_result)
    
    env_result = check_env_files(url)
    if env_result:
        findings.update(env_result)

    # Display fix suggestions
    print_suggestions(findings)
    
    print("\nScan complete.\n")

if __name__ == "__main__":
    main()

