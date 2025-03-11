from flask import Flask, jsonify
from libs.api import buscar_cep
from libs.banco import inserir_tabela, view_tabela
app = Flask(__name__)

@app.route('/buscar_cep/<cep>', methods=['GET'])
def buscar(cep):
    retorno = buscar_cep(cep)
    
    if not retorno:
        return jsonify({'erro': 'CEP inválido'}), 404 # erro

    dados = retorno
    if dados:
        inserir_tabela(
            cep=dados.get('cep'),
            logradouro=dados.get('logradouro'),
            complemento=dados.get('complemento'),
            unidade=dados.get('unidade'),
            bairro=dados.get('bairro'),
            localidade=dados.get('localidade'),
            uf=dados.get('uf'),
            estado=dados.get('estado'),
            regiao=dados.get('regiao'),
            ibge=dados.get('ibge'),
            gia=dados.get('gia'),
            ddd=dados.get('ddd'),
            siafi=dados.get('siafi')
        )
    return jsonify(retorno)

@app.route('/ver_tabela', methods=['POST', 'GET'])
def ver_tabela():
    dados = view_tabela()
    dados2 = []

    for item in dados:
        dados2.append({
            "cep": item[0],
            "logradouro": item[1],
            "complemento": item[2],
            "unidade": item[3],
            "bairro": item[4],
            "localidade": item[5],
            "uf": item[6],
            "estado": item[7],
            "regiao": item[8],
            "ibge": item[9],
            "gia": item[10],
            "ddd": item[11],
            "siafi": item[12]
        })
    return jsonify(dados2)

if __name__ == '__main__':
    app.run(debug=True, port=7777)