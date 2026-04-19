# dados estruturados - criação
# excel

import pandas as pcd

dados1 = {
    'nome': ['Stalin', 'Barack Obama', 'Bolsonaro'],
    'idade': [102, 11, 54],
    'cidade': ['Moskou', 'Nova York', "Berlim"]
}

df_planilha1 = pcd.DataFrame(dados1)

with pcd.ExcelWriter("manipulacao_dados/criacaoELeituraDeDados/dadosEstruturados1.xlsx") as writer:
    df_planilha1.to_excel(writer, sheet_name='Planilha1', index=False,)