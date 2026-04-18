# SQL_ALCHEMY
# Permite a conexão da API ao banco de dados
# pip install flask_sqlalchemy

from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask('carros')

# Rastrear as modificações realizadas
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Configuração de conexão com o bd
# 1- usuario (root) 
# 2- Senha (Senai@134) 
# 3- localhost (127.0.0.1)
# 4- nome do banco (db_carro)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Senai%40134@127.0.0.1/db_carro' # %40 = @

mybd = SQLAlchemy(app)

# Classe para definir o modelo dos dados que correspondem a tabela do banco de dados
class Carros(mybd.Model):
    __tablename__ = 'tb_carro'
    id_carro = mybd.Column(mybd.Integer, primary_key = True)
    marca = mybd.Column(mybd.String(255))
    modelo = mybd.Column(mybd.String(255))
    ano = mybd.Column(mybd.String(255))
    cor = mybd.Column(mybd.String(255))
    valor = mybd.Column(mybd.String(255))
    numero_vendas = mybd.Column(mybd.String(255))

    def to_json(self):
        return {
            "id_carro": self.id_carro,
            "marca": self.marca,
            "modelo": self.modelo,
            "ano": self.ano,
            "valor": float(self.valor),
            "cor": self.cor,
            "numero_vendas": self.numero_vendas
        }

# -----------------------------------------------------------------------------------------------------

# METODOS
# GET
@app.route('/carros', methods=['GET'])
def get_carros():
    # Executa uma consulta no banco de dados
    carro_selecionado = Carros.query.all()
    # Transforma o objeto de linhas e colunas para json
    carro_json = [carro.to_json() for carro in carro_selecionado]   
    return gera_resposta(200, carro_json)

# GET ID
@app.route('/carros/<id_carro_pam>',  methods=['GET'])
def get_carro_id(id_carro_pam):
    carro_selecionado = Carros.query.filter_by(id_carro = id_carro_pam).first()
    carro_json = carro_selecionado.to_json()
    return gera_resposta(200, carro_json)

# POST
@app.route('/carros', methods=['POST'])
def criar_carro():
    requisicao = request.get_json()
    try:
        carro = Carros(
            id_carro = requisicao['id_carro'],
            marca = requisicao['marca'],
            modelo = requisicao['modelo'],
            ano = requisicao['ano'],
            cor = requisicao['cor'],
            valor = requisicao['valor'],
            numero_vendas = requisicao['numero_vendas']
        )

        # Faz um insert ao banco de dados
        mybd.session.add(carro)
        # Salva no banco de dados
        mybd.session.commit()

        return gera_resposta(201, carro.to_json(), 'POST realizado com sucesso')
    
    except Exception as e:
        print('Erro', e)

        return gera_resposta(400, {}, "Erro ao realizar o POST")

# DELETE
@app.route('/carros/<id_carro_p>', methods=['DELETE'])
def deleta_carro(id_carro_p):
    carro = Carros.query.filter_by(id_carro = id_carro_p).first()

    try:
        # Deleta o registro selecionado
        mybd.session.delete(carro)
        mybd.session.commit()
        return gera_resposta(200, carro.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_resposta(400, {}, "Erro ao realizar o DELETE")

# UPDATE
@app.route("/carros/<id_carro_p>", methods=['PUT'])
def atualiza_carro(id_carro_p):
    carro = Carros.query.filter_by(id_carro = id_carro_p).first()
    requisicao = request.get_json()

    try:
        if('marca' in requisicao):
            carro.marca = requisicao['marca']

        if('modelo' in requisicao):
            carro.modelo = requisicao['modelo']

        if('ano' in requisicao):
            carro.ano = requisicao['ano']
        
        if('valor' in requisicao):
            carro.valor = requisicao['valor']

        if('cor' in requisicao):
            carro.cor = requisicao['cor']

        if('numero_vendas' in requisicao):
            carro.numero_vendas = requisicao['numero_vendas']

        mybd.session.add(carro)
        mybd.session.commit()
            
        return gera_resposta(200, carro.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_resposta(400, {}, "Erro ao realizar o PUT")


# Resposta Padrão
def gera_resposta(status, conteudo, mensagem=False):
    body = {}

    body['Lista de Carro'] = conteudo

    if(mensagem):
        body['mensagem'] = mensagem

    # dumps converte o array em json
    return Response(json.dumps(body), status=status, mimetype='application/json')


app.run(port=5000, host='localhost', debug=True)

