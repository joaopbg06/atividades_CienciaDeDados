# 2. Escreva um programa que leia um número inteiro positivo e determine se ele é um
# palíndromo (ou seja, se lido de trás para frente continua igual).
# Exemplo:
#  Entrada: 1221
#  Saída: 1221 é um número palíndromo


entrada = input('Insira um número: ')
y = ''

for x in entrada:
    y =  x + y

if y == entrada:
    print("Este número é um palíndromo")
else:
    print("Este número não é um palíndromo")
