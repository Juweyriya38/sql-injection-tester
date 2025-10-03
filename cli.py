# cli.py

import argparse
from scanner.tester import test_url_for_sqli
from scanner.report import save_results

def main():
    parser = argparse.ArgumentParser(description="SQL Injection Tester")
    parser.add_argument("--url", required=True, help="Target base URL (e.g., http://example.com/page)")
    parser.add_argument("--param", default="id", help="Query parameter to test (default: id)")
    args = parser.parse_args()
    
    print(f"\n[+] Testing {args.url} for SQL Injection on parameter '{args.param}'...\n")
    results = test_url_for_sqli(args.url, args.param)
    save_results(results)

if __name__ == "__main__":
    main()
