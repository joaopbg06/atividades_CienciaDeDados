import pandas as pcd

df_nao = pcd.read_csv('manipulacao_dados/criacaoELeituraDeDados/dadosNao.csv')

print(df_nao['cidade'])