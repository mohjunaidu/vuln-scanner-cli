from colorama import Fore, Style

def print_suggestions(findings):
    """Print fix suggestions based on scan findings"""
    
    print(Fore.CYAN + "\n" + "="*60)
    print("🔧 FIX SUGGESTIONS")
    print("="*60 + Style.RESET_ALL + "\n")
    
    # Security Headers Suggestions
    if findings.get('missing_headers'):
        print(Fore.YELLOW + "[!] Missing Security Headers Detected" + Style.RESET_ALL)
        print("\nAdd the following headers to your web server configuration:\n")
        
        suggestions = {
            "Content-Security-Policy": {
                "description": "Prevents XSS attacks by controlling resource loading",
                "example": "Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'"
            },
            "X-Frame-Options": {
                "description": "Prevents clickjacking attacks",
                "example": "X-Frame-Options: DENY  (or SAMEORIGIN)"
            },
            "X-XSS-Protection": {
                "description": "Enables browser XSS filter (legacy, but still useful)",
                "example": "X-XSS-Protection: 1; mode=block"
            },
            "Strict-Transport-Security": {
                "description": "Forces HTTPS connections (HSTS)",
                "example": "Strict-Transport-Security: max-age=31536000; includeSubDomains"
            },
            "X-Content-Type-Options": {
                "description": "Prevents MIME type sniffing",
                "example": "X-Content-Type-Options: nosniff"
            },
            "Referrer-Policy": {
                "description": "Controls referrer information sent",
                "example": "Referrer-Policy: strict-origin-when-cross-origin"
            }
        }
        
        for header in findings['missing_headers']:
            if header in suggestions:
                print(Fore.GREEN + f"  • {header}" + Style.RESET_ALL)
                print(f"    Purpose: {suggestions[header]['description']}")
                print(f"    Example: {Fore.CYAN}{suggestions[header]['example']}{Style.RESET_ALL}\n")
        
        print(Fore.CYAN + "  Implementation:" + Style.RESET_ALL)
        print("  - Apache: Add to .htaccess or httpd.conf")
        print("  - Nginx: Add to server block in nginx.conf")
        print("  - Express.js: Use helmet middleware")
        print("  - Django: Use django.middleware.security.SecurityMiddleware\n")
    
    # Server Info Disclosure
    if findings.get('server_disclosed') and findings['server_disclosed'] != "Not disclosed":
        print(Fore.YELLOW + "[!] Server Information Disclosure" + Style.RESET_ALL)
        print(f"\nServer header reveals: {Fore.RED}{findings['server_disclosed']}{Style.RESET_ALL}\n")
        print("  Recommendations:")
        print("  • Hide or remove the Server header")
        print("  • Apache: Set 'ServerTokens Prod' in httpd.conf")
        print("  • Nginx: Remove or modify server_tokens directive")
        print("  • Consider using a reverse proxy to mask server info\n")
    
    # Exposed Environment Files
    if findings.get('exposed_files'):
        print(Fore.RED + "[!] CRITICAL: Exposed Sensitive Files" + Style.RESET_ALL)
        print("\nThe following sensitive files are publicly accessible:\n")
        for file_path in findings['exposed_files']:
            print(f"  {Fore.RED}✗ {file_path}{Style.RESET_ALL}")
        print("\n  Immediate Actions:")
        print("  • Remove these files from public web root")
        print("  • Move .env files outside web-accessible directories")
        print("  • Ensure .git directory is not in web root")
        print("  • Delete or secure backup files")
        print("  • Add to .gitignore if version controlled")
        print("  • Configure web server to deny access to sensitive file patterns\n")
    
    # Directory Enumeration Findings
    if findings.get('accessible_dirs'):
        print(Fore.YELLOW + "[!] Accessible Directories Found" + Style.RESET_ALL)
        print(f"\nFound {len(findings['accessible_dirs'])} accessible directory(ies):\n")
        for dir_path in findings['accessible_dirs'][:5]:  # Show first 5
            print(f"  • {dir_path}")
        if len(findings['accessible_dirs']) > 5:
            print(f"  ... and {len(findings['accessible_dirs']) - 5} more")
        print("\n  Recommendations:")
        print("  • Review if these directories should be publicly accessible")
        print("  • Implement access controls (authentication/authorization)")
        print("  • Add directory listing protection (Options -Indexes in Apache)")
        print("  • Use .htaccess or nginx rules to restrict access")
        print("  • Consider moving sensitive directories outside web root\n")
    
    # Summary
    total_issues = (
        len(findings.get('missing_headers', [])) +
        (1 if findings.get('server_disclosed') and findings['server_disclosed'] != "Not disclosed" else 0) +
        len(findings.get('exposed_files', [])) +
        len(findings.get('accessible_dirs', []))
    )
    
    if total_issues == 0:
        print(Fore.GREEN + "✓ No critical issues found! Your security headers look good." + Style.RESET_ALL + "\n")
    else:
        print(Fore.YELLOW + f"\n📊 Summary: {total_issues} security issue(s) identified" + Style.RESET_ALL)
        print("Prioritize fixing exposed files first, then missing headers.\n")

