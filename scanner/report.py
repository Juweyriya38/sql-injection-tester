# scanner/report.py

import json

def save_results(results, filename="sqli_report.json"):
    formatted = [
        {"url": url, "vulnerable": vuln}
        for url, vuln in results
    ]
    with open(filename, "w") as f:
        json.dump(formatted, f, indent=4)
    print(f"\n[+] Results saved to {filename}")
