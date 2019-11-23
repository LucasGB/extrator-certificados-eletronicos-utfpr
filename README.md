
# Extrator de Certificados Eletrônicos da UTFPR

Uma ferramenta para extração de certificados eletrônicos da Universidade Tecnológica Federal do Paraná, disponíveis em http://apl.utfpr.edu.br/extensao/certificados/listaPublica.

## Instalação
É recomendável utilizar o virtualenv para isolar dependências sem interferir no seu sistema operacional ou nos demais projetos.

 __Passo 1:__ Crie o ambiente virtual
* No terminal, navegue até a raiz do projeto e execute o seguinte comando:
```
virtualenv env
```

__Passo 2:__ Ative o ambiente virtual
```
env\Scripts\activate
```

__Passo 3:__ Instale as dependências do projeto

```
pip install -r requirements.txt
```

## Uso
Na raiz do projeto, execute o seguinte comando:

```
python3 main.py
```

