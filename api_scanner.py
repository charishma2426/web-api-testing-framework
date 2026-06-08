import requests

class APISecurityScanner:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')
        print(f"[*] Target Loaded Successfully: {self.base_url}\n")

    def test_bola_idor(self):
        print("[+] Starting Test 1: Checking for BOLA/Data Leaks...")
        for user_id in [1, 2, 3]:
            test_url = f"{self.base_url}/users/{user_id}"
            response = requests.get(test_url)
            if response.status_code == 200:
                print(f"    [ALERT] Success! We accessed private data for User #{user_id} at: {test_url}")
            else:
                print(f"    [OK] Could not access User #{user_id} (Status: {response.status_code})")
        print("-" * 50)

    def test_security_headers(self):
        print("[+] Starting Test 2: Checking Server Security Headers...")
        try:
            response = requests.get(self.base_url)
            headers = response.headers
            
            important_headers = ['X-Content-Type-Options', 'X-Frame-Options', 'Content-Security-Policy']
            
            for header in important_headers:
                if header in headers:
                    print(f"    [OK] Found protective header: {header}")
                else:
                    print(f"    [WARN] MISSING critical header: {header}")
                    
        except requests.RequestException as e:
            print(f"    [!] Connection error: {e}")
        print("-" * 50)

# CRITICAL: Make sure these lines are all the way to the left edge!
if __name__ == "__main__":
    TARGET = "https://jsonplaceholder.typicode.com"
    
    scanner = APISecurityScanner(TARGET)
    
    scanner.test_bola_idor()
    scanner.test_security_headers()