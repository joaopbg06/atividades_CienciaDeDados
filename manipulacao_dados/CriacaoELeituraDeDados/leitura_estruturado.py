import pandas as pcd

df_estruturado = pcd.read_excel('manipulacao_dados/criacaoELeituraDeDados/dadosEstruturados1.xlsx', sheet_name='Planilha1')

print(df_estruturado)