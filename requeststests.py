import requests


r = requests.get("https://google.com")
print("Status:", r.status_code)
print(r.url)
print(r.text)

f = open("./page.html", "w+")
f.write(r.text)
