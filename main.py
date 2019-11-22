from bs4 import BeautifulSoup
import requests

campus = '3'
ano = ''
evento = ''
nome = 'Lucas Guedes Barboza'
hdnPesquisa = 'pesquisa'
cmbPesquisa = 'D'

url = 'http://apl.utfpr.edu.br/extensao/certificados/listaPublica'
_params = {'txtCampus' : campus, 'txtAno' : ano, 'txtEvento' : evento}

html_doc = requests.post(url, data=_params)

soup = BeautifulSoup(html_doc.text, 'html.parser')

events_dropdown = soup.find('select', {'name' : 'txtEvento'})

events = []

for option in events_dropdown.find_all('option'):
	events.append(option['value'])

del events[0]

'''for event in events:
	_params = {'txtCampus' : '3', 'txtAno' : '', 'txtEvento' : event}
	html_doc = requests.post(url, data=_params)

	soup = BeautifulSoup(html_doc.text, 'html.parser')

	print(soup.prettify())'''

_params = {'txtCampus' : campus, 'txtAno' : ano, 'txtEvento' : 585, 'hdnPesquisa' : hdnPesquisa, 'cmbPesquisa' : cmbPesquisa, 'txtPesquisa' : nome}
html_doc = requests.post(url, data=_params)

soup = BeautifulSoup(html_doc.text, 'html.parser')

print(soup.prettify())