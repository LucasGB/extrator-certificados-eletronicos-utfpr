from bs4 import BeautifulSoup
import requests
import os

if not os.path.exists('certificados'):
	os.makedirs('certificados')

nome = input("Digite seu nome: ")
campi = {'Curitiba' : 1, 'Apucarana' : 2, 'Campo Mourão' : 3, 'Dois Vizinhos' : 4, 'Francisco Beltrão' : 5, 'Guarapuava' : 6, 'Lodrina' : 7, 'Medianeira' : 8, 'Pato Branco' : 9, 'Ponta Grossa' : 10, 'Santa Helena' : 11, 'Toledo' : 12, 'Cornélio Procópio' : 13}
campus = input('Digite seu campus: ')
while(campus not in campi):
	print('Entrada inválida.')
	campus = input('Digite seu campus: ')

campus = campi.get(campus)
ano = ''
evento = ''
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
