import requests
import logging

############################################

############################################

logging.basicConfig(level=logging.DEBUG)
try:
	#response = requests.get("http://localhost/index.html")
	#print(response)
	print (1)
except ConnectionRefusedError:
	print ("ConnectionRefusedError")


log = open("/var/log/nginx/nginx_error.log", "r")

for line in log:
    print(line)