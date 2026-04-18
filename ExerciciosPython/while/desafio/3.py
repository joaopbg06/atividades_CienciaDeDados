# 3. Escreva um programa que leia um número inteiro e conte quantos dígitos ele tem.
# Exemplo:
#  Entrada: 98765
#  Saída: O número 98765 tem 5 dígitos

x = input('Insira um número: ').strip()
cont = 0

for i in x:
    cont += 1

print(f'Este número tem {cont} dígitos')