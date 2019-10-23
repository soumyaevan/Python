import requests
res = requests.get("https://www.google.com")
print(res)
print(res.ok)
print(res.headers)
print(res.status_code)