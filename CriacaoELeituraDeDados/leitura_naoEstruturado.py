import pandas as pcd

df_nao = pcd.read_csv('dadosNao.csv')

print(df_nao['cidade'])