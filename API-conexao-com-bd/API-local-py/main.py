# pip install flask
from flask import Flask, request, make_response, jsonify

#Importar banco de dados
from bd import Carros

app = Flask('carros')

# GET
@app.route('/car', methods=['GET'])

def get_carros():
    return Carros

@app.route('/car/<int:id>', methods=['GET'])
def get_carros_id(id):
    for carro in Carros:
        if carro.get('id') == id:
            return jsonify(carro)

# POST
@app.route('/car', methods=['POST'])
def post_carros():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(
            mensagem = 'Carro cadastrado com sucesso!',
            car = carro
        )
    )

# DELETE
@app.route('/car/<int:id>', methods=['DELETE'])
def excluir_carro(id):
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            del Carros[indice]
            return jsonify(
                {'mensagem': 'Carro excluído'}
            )

# PUT
@app.route('/car/<int:id>', methods=['PUT'])
def editar_carro(id):
    carro_alterado = request.get_json()
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            Carros[indice].update(carro_alterado)
            return jsonify(
                Carros[indice]
            )


app.run(port=5000, host='localhost', debug=True)