import requests
from bs4 import BeautifulSoup

url = 'http://apl.utfpr.edu.br/extensao/certificados/listaPublica'
myobj = {'txtCampus' : '3', 'txtAno' : '', 'txtEvento' : '828'}

html_doc = requests.post(url, data = myobj)


soup = BeautifulSoup(html_doc.text, 'html.parser')

print(soup.prettify())

