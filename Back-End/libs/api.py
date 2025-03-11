import requests
import json

def buscar_cep(cep):
    retorno = requests.get(url= f'https://viacep.com.br/ws/{cep}/json/')
    retorno = json.loads(retorno.text)
    return retorno