print("Welcome guys, today i will show you how you can get your ip with python")

# first we will import request library

import requests


# this will send a get request to the website and the website will return the ip
r = requests.get("https://httpbin.org/ip")
print(r.text)


# now lets test it