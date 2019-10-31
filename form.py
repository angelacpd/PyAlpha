import requests

my_data = {"name": "Angela", "email": "angela@protonmail.com"}
r = requests.post("https://tryphp.w3schools.com/demo_form_post.php", data=my_data)

print("Status code:", r.status_code)

f = open("myfile.html", "w+")
f.write(r.text)
