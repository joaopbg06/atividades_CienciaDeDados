import pandas as pcd

dados2 = {
    'nome': ['Stalin', 'Barack Obama', 'Bolsonaro'],
    'idade': [102, 11, 54],
    'cidade': ['Moskou', 'Nova York', "Berlim"]
}

df_json = pcd.DataFrame(dados2)

df_json.to_json('manipulacao_dados/criacaoELeituraDeDados/dadosSemi.json', orient='records', lines=False)