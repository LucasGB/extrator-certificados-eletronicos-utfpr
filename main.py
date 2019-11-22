import requests
from bs4 import BeautifulSoup

url = 'http://apl.utfpr.edu.br/extensao/certificados/listaPublica'
#_params = {'txtCampus' : '3', 'txtAno' : '', 'txtEvento' : '828'}
_params = {'txtCampus' : '3', 'txtAno' : '', 'txtEvento' : ''}

html_doc = requests.post(url, data = _params)

soup = BeautifulSoup(html_doc.text, 'html.parser')

a = soup.find('select', {'name' : 'txtEvento'}).attrs

print(a)


#print(soup.prettify())