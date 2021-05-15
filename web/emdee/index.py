from bs4 import BeautifulSoup
import requests
import hashlib

url = "example.com" # pass host url
http_with_one_connection = requests.session()
response_get = http_with_one_connection.get(url)

hash = hashlib.md5(BeautifulSoup(response_get.text).h3.string.encode('utf-8')).hexdigest()

response_post = http_with_one_connection.post(url,

  data = dict(hash=hash),

  headers = {

    'Content-Type':'application/x-www-form-urlencoded',

  }

)
print(response_post.text)
