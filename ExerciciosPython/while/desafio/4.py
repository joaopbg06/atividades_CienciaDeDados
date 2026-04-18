# 4. Escreva um programa que leia um número inteiro positivo e determine se ele é um número
# perfeito. Um número perfeito é aquele cuja soma dos seus divisores próprios (excluindo ele
# mesmo) é igual ao próprio número.
# Exemplo:
#  Entrada: 28
#  Cálculo: 1 + 2 + 4 + 7 + 14 = 28
#  Saída: 28 é um número perfeito

entrada = int(input('Insira um número: '))
soma = 0


for i in range(1, entrada):
    if entrada % i == 0:
        soma += i

if soma == entrada:
    print('Entre número é perfeito')
else:
    print('Entre número NÃO é perfeito')
    