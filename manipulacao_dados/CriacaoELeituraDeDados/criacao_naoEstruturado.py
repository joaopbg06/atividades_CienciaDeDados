import pandas as pcd

dados3 = {
    'nome': ['Stalin', 'Barack Obama', 'Bolsonaro'],
    'idade': [102, 11, 54],
    'cidade': ['Moskou', 'Nova York', "Berlim"]
}

df_csv = pcd.DataFrame(dados3)

df_csv.to_csv('manipulacao_dados/criacaoELeituraDeDados/dadosNao.csv', index=False)