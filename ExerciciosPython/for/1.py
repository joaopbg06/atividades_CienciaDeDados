# 1. Faça um programa que leia 5 números e informe o maior número.

lista = []

for i in range(5):
    num = int(input('Insira um número: '))
    lista.append(num)

maior = 1

for i in lista:
    if i > maior:
        maior = i

print(f'O maior número é {maior}')