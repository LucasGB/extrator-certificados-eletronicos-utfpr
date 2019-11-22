from bs4 import BeautifulSoup
import requests

campus = '3'
ano = ''
evento = ''
nome = 'Lucas Guedes Barboza'
hdnPesquisa = 'pesquisa'
cmbPesquisa = 'D'
events = []

url = 'http://apl.utfpr.edu.br/extensao/certificados/listaPublica'
_params = {'txtCampus' : campus, 'txtAno' : ano, 'txtEvento' : evento}

html_doc = requests.post(url, data=_params)
soup = BeautifulSoup(html_doc.text, 'html.parser')
events_dropdown = soup.find('select', {'name' : 'txtEvento'})

for option in events_dropdown.find_all('option'):
	events.append(option['value'])
del events[0]

for event in events:
	jobs = []

	_params = {'txtCampus' : campus, 'txtAno' : ano, 'txtEvento' : event, 'hdnPesquisa' : hdnPesquisa, 'cmbPesquisa' : cmbPesquisa, 'txtPesquisa' : nome}
	html_doc = requests.post(url, data=_params)

	soup = BeautifulSoup(html_doc.text, 'html.parser')

	# Retrieves the text from the h3 tag, cleaning unwanted default text.
	#titulo = soup.find('div', {'class' : 'titulo_right'}).h3.text.strip('Listagem de Certificados - ').replace('-', ' ')
	titulo = soup.find('div', {'class' : 'titulo_right'}).h3.text.replace('Listagem de Certificados - ', '')
	print(titulo)

	for a in soup.find_all('a', href=True):
		certificate = a['href'].replace('certificados/validar', 'emitir')
		jobs.append(certificate)

	# Downloads PDF files appending (<number) at the end of the string whenver multiple results are found.
	for i in range(len(jobs)):
		file = requests.get(jobs[i], allow_redirects=True)

		if(i != 0):
			with open('certificados/{}({}).pdf'.format(titulo, i), 'wb') as f:
				f.write(file.content)
		else:
			with open('certificados/{}.pdf'.format(titulo), 'wb') as f:
				f.write(file.content)
