from time import sleep
from requests import get 

endpoint = "https://api-gt-services.juanengml.repl.co"

list_endpoints = ["/api/v1/coffe/ativos","/api/v1/food/ativos",
"/api/v1/address/ativos","/api/v1/blood/ativos"]

while True:
 for endpt in list_endpoints:
  url = endpoint + endpt
  print(url)
  r = get(url).json()
  print(r)
sleep(10)