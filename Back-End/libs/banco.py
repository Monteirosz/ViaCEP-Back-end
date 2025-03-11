import sqlite3

def criar_tabela():
    con = sqlite3.connect('banco_cep.db')
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS CEPAPI')

    comando = '''CREATE TABLE CEPAPI (
        CEP VAR(200) NOT NULL,
        LOGRADOURO TEXT,
        COMPLEMENTO TEXT,
        UNIDADE TEXT,
        BAIRRO TEXT,
        LOCALIDADE TEXT,
        UF TEXT,
        ESTADO TEXT,
        REGIAO TEXT,
        IBGE TEXT,
        GIA TEXT,
        DDD TEXT,
        SIAFI TEXT
        )'''

    cur.execute(comando)
    con.close()

def view_tabela():
    con = sqlite3.connect('banco_cep.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM CEPAPI")
    dados = cur.fetchall()
    con.close()
    return dados

def inserir_tabela(cep, logradouro, complemento, unidade, bairro, localidade, uf, estado, regiao, ibge, gia, ddd, siafi):
    con = sqlite3.connect('banco_cep.db')
    cur = con.cursor()
    cur.execute('INSERT INTO CEPAPI (CEP, LOGRADOURO, COMPLEMENTO, UNIDADE, BAIRRO, LOCALIDADE, UF, ESTADO, REGIAO, IBGE, GIA, DDD, SIAFI) values(?,?,?,?,?,?,?,?,?,?,?,?,?)', (cep, logradouro, complemento, unidade, bairro, localidade, uf, estado, regiao, ibge, gia, ddd, siafi))
    con.commit()
    con.close()

criar_tabela()