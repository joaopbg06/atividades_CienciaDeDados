# 4. Faça um programa que leia 5 números e informe a soma e a média dos
# números.

lista = []

for i in range(5):
    num = int(input('Insira um número: '))
    lista.append(num)

soma = 0

for i in lista:
    soma += i

print(f"A soma total é: {soma}")
print(f"A média é: {soma/5}")