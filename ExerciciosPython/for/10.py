# 10. Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja A
# foi superior a loja B (faturamento = 54000). Se o faturamento atingir esse
# valor mostre na tela uma mensagem contendo em quanto foi superado o
# faturamento.


faturamentoA = 0 

for i in range(5):
    valor = int( input('Insira o valor da venda: '))
    faturamentoA += valor
    


if faturamentoA >= 54000:
    print(f"O faturamento foi superado em {faturamentoA - 54000}")

