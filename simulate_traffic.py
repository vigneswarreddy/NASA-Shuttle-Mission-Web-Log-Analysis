import time
import requests
import re

LOG_FILE = "logs/nasa_access_log_Jul95.log"
BASE_URL = "http://localhost:80"  # Pointing to your NGINX reverse proxy
path_pattern = r'"GET (.*?) HTTP'

with open(LOG_FILE, "r", encoding="latin-1") as f:
    for line in f:
        match = re.search(path_pattern, line)
        if match:
            path = match.group(1).strip()
            
            # Optional: Skip irrelevant or empty paths
            if not path or path == "/":
                continue

            full_url = BASE_URL + path
            try:
                r = requests.get(full_url)
                print(f"Sent GET {path} | Status: {r.status_code}")
                time.sleep(0.5)  # Simulate traffic interval
            except Exception as e:
                print(f"Failed to GET {path}: {e}")
