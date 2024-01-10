import requests
import time

url = "http://127.0.0.1:8000/user"  


payload = {"address": "حدائق القبة"}

# Send HTTP request and measure execution time
start_time = time.time()
response = requests.get(url, params=payload)
end_time = time.time()

# Print results
print(f"Response: {response.text}")
print(f"Execution Time: {end_time - start_time} seconds (Note that this time of request that work based on two methodology parallel and not)")
