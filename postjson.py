import requests
import simplejson as json

url = "https://developers.google.com/url-shortener/v1/url"
payload = {"longUrl": "http://example.com/"}
headers = {"Content-Type": "application/json"}
r = requests.post(url, json=payload, headers=headers)

print(r.text)
