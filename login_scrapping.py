import requests
from bs4 import BeautifulSoup

requests_session = requests.Session()

payload = {
	'email': 'miteshbhanushali08@gmail.com',
	'password': 'test@1234',
	'_formname' : 'login'
}
## step-1 : request login page
login = requests_session.get("https://www.codeheroku.com/login");
login_status = BeautifulSoup(login.content,'html.parser')

## step-2 : get the formkey
_formkey = login_status.find(attrs={"name":"_formkey"})['value']
payload['_formkey'] = _formkey

## step-3 : submit data and store into session
result = requests_session.post('https://www.codeheroku.com/login',data=payload)
print(result)

## step-4 : request dashboard page 
navigate_to_dashbord = requests_session.get('https://www.codeheroku.com/dashboard')
print(navigate_to_dashbord)