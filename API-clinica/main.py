from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask('db_clinica')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Senai%40134@127.0.0.1/clinicavetbd'

mybd = SQLAlchemy(app)

class Cliente(mybd.Model):
    __tablename__ = 'tb_clientes'
    id_cliente = mybd.Column(mybd.Integer, primary_key = True)
    nome = mybd.Column(mybd.String(255))
    endereco = mybd.Column(mybd.String(255))
    telefone = mybd.Column(mybd.String(255))

    def to_json(self):
        return {
            "id_cliente": self.id_cliente,
            "nome": self.nome,
            "endereco": self.endereco,
            "telefone": self.telefone
        }
    
class Pets(mybd.Model):
    __tablename__ = 'tb_pets'
    id_pet = mybd.Column(mybd.Integer, primary_key = True)
    nome = mybd.Column(mybd.String(255))
    tipo = mybd.Column(mybd.String(255))
    raca = mybd.Column(mybd.String(255))
    data_nascimento = mybd.Column(mybd.String(255))
    id_cliente = mybd.Column(mybd.Integer, mybd.ForeignKey('tb_clientes.id_cliente'), nullable=False)
    idade = mybd.Column(mybd.String(255))

    def to_json(self):
        return {
            "id_pet": self.id_pet,
            "nome": self.nome,
            "tipo": self.tipo,
            "raca": self.raca,
            "data_nascimento": str(self.data_nascimento),
            "id_cliente": self.id_cliente,
            "idade": self.idade
        }
    
# ------------------
# GET

@app.route('/clientes' , methods=["GET"])
def selecionar_clientes():
    clientes_selecionados = Cliente.query.all()
    clientes_json = [cliente.to_json() for cliente in clientes_selecionados]
    return gera_resposta(200, 'Clientes', clientes_json)

@app.route('/pets' , methods=["GET"])
def selecionar_pets():
    pets_selecionados = Pets.query.all()
    pets_json = [cliente.to_json() for cliente in pets_selecionados]
    return gera_resposta(200, 'Pets', pets_json)

# GET ID

@app.route('/clientes/<id_cliente_p>',  methods=["GET"])
def selecionar_cliente_id(id_cliente_p):
    cliente_selecionado = Cliente.query.filter_by(id_cliente = id_cliente_p).first()
    cliente_json = cliente_selecionado.to_json()
    return gera_resposta(200, 'Cliente',cliente_json)

@app.route('/pets/<id_pet_p>',  methods=["GET"])
def selecionar_pet_id(id_pet_p):
    pet_selecionado = Pets.query.filter_by(id_pet = id_pet_p).first()
    pet_json = pet_selecionado.to_json()
    return gera_resposta(200, 'Pet', pet_json)

# POST 

@app.route('/clientes', methods=["POST"])
def adicionar_cliente():
    body = request.get_json()
    try:
        cliente = Cliente(
            id_cliente = body['id_cliente'],
            nome = body['nome'],
            endereco = body['endereco'],
            telefone = body['telefone']
        )

        mybd.session.add(cliente)
        mybd.session.commit()

        return gera_resposta(201, 'Cliente inserido',cliente.to_json(), "POST realizado com sucesso")
    except Exception as e :
        print('Erro', e)
        return gera_resposta(400, '', {}, 'Erro ao realizar o POST')

@app.route('/pets', methods=["POST"])
def adicionar_pet():
    body = request.get_json()
    try:
        pet = Pets(
            id_pet = body['id_pet'],
            nome = body['nome'],
            tipo = body['tipo'],
            raca = body['raca'],
            data_nascimento = body['data_nascimento'],
            id_cliente = body['id_cliente'],
            idade = body['idade']
        )

        mybd.session.add(pet)
        mybd.session.commit()

        return gera_resposta(201, 'Cliente inserido', pet.to_json(), "POST realizado com sucesso")
    except Exception as e :
        print('Erro', e)
        return gera_resposta(400, '', {}, 'Erro ao realizar o POST')

# DELETE

@app.route("/clientes/<id_cliente_p>", methods=['DELETE'])
def deletar_cliente(id_cliente_p):
    cliente_del = Cliente.query.filter_by(id_cliente = id_cliente_p).first()
    try:
        mybd.session.delete(cliente_del)
        mybd.session.commit()
        return gera_resposta(201, 'Cliente deletado', cliente_del.to_json(), "DELETE realizado com sucesso")
    
    except Exception as e :
        print('Erro', e)
        return gera_resposta(400, '', {}, 'Erro ao realizar o DELETE')

@app.route("/pets/<id_pet_p>", methods=['DELETE'])
def deletar_pet(id_pet_p):
    pet_del = Pets.query.filter_by(id_pet = id_pet_p).first()
    try:
        mybd.session.delete(pet_del)
        mybd.session.commit()
        return gera_resposta(201, 'Pet deletado', pet_del.to_json(), "DELETE realizado com sucesso")
    
    except Exception as e :
        print('Erro', e)
        return gera_resposta(400, '', {}, 'Erro ao realizar o DELETE')

# PUT

@app.route("/clientes/<id_cliente_p>", methods=['PUT'])
def atualizar_cliente(id_cliente_p):
    cliente_put = Cliente.query.filter_by(id_cliente = id_cliente_p).first()
    body = request.get_json()

    try:
        if('nome' in body):
            cliente_put.nome = body['nome']
        if('endereco' in body):
            cliente_put.endereco = body['endereco']
        if('telefone' in body):
            cliente_put.telefone = body['telefone']
        
        mybd.session.add(cliente_put)
        mybd.session.commit()

        return gera_resposta(201, 'Cliente Atualizado', cliente_put.to_json(), "PUT realizado com sucesso")

    except Exception as e :
        print('Erro', e)
        return gera_resposta(400, '', {}, 'Erro ao realizar o DELETE')

@app.route("/pets/<id_pet_p>", methods=['PUT'])
def atualizar_pets(id_pet_p):
    pet_put = Pets.query.filter_by(id_pet= id_pet_p).first()
    body = request.get_json()

    try:
        if('nome' in body):
            pet_put.nome = body['nome']
        if('tipo' in body):
            pet_put.tipo = body['tipo']
        if('raca' in body):
            pet_put.raca = body['raca']
        if('data_nascimento' in body):
            pet_put.data_nascimento = body['data_nascimento']
        if('id_cliente' in body):
            pet_put.id_cliente = body['id_cliente']
        if('idade' in body):
            pet_put.idade = body['idade']
        
        mybd.session.add(pet_put)
        mybd.session.commit()

        return gera_resposta(201, 'Pet Atualizado', pet_put.to_json(), "PUT realizado com sucesso")

    except Exception as e :
        print('Erro', e)
        return gera_resposta(400, '', {}, 'Erro ao realizar o DELETE')

# ------------------
def gera_resposta(status, nome_conteudo, conteudo, mensagem=False):
    body = {}

    body[nome_conteudo] = conteudo

    if(mensagem):
        body['Mensagem'] = mensagem

    return Response(json.dumps(body), status=status, mimetype='application/json') 

app.run(port=5000, host='localhost', debug=True)