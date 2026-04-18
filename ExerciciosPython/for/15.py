# 15. Uma loja tem tem uma política de descontos de acordo com o valor da
# compra do cliente. Os descontos começam acima dos R$500. A cada 100
# reais acima dos R$500,00 o cliente ganha 1% de desconto cumulativo até
# 25%.
# Por exemplo: R$500 = 1% || R$600,00 = 2% … etc…
# Faça um programa que exiba essa tabela de descontos no seguinte formato:
# Valordacompra – porcentagem de desconto – valor final

valor = 400
desconto = 0
final = 0


for i in range(30):
    valor += 100
    if desconto < 0.25:
        desconto += 0.01
    final = valor - (valor * desconto)

    print(f"Valor da compra: {valor} || porcentagem do desconto: {desconto * 100:0.2f}% || valor final: {final:0.2f}")