# scanner/tester.py

import requests
from scanner.payloads import get_sqli_payloads

def test_url_for_sqli(base_url, param="id"):
    payloads = get_sqli_payloads()
    results = []

    for payload in payloads:
        test_url = f"{base_url}?{param}={payload}"
        try:
            response = requests.get(test_url, timeout=5)
            if any(err in response.text.lower() for err in ["sql", "syntax", "mysql", "error", "query"]):
                results.append((test_url, True))
                print(f"[!] Vulnerable: {test_url}")
            else:
                results.append((test_url, False))
                print(f"[-] Safe: {test_url}")
        except requests.exceptions.RequestException as e:
            print(f"[x] Error testing {test_url}: {e}")
            results.append((test_url, None))

    return results
