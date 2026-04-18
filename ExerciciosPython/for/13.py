# 13. Faça um programa que peça 10 números inteiros, calcule e mostre a
# quantidade de números pares e a quantidade de números impares.


lista = []
par = 0
impar = 0

for i in range(10):
    num = int(input('Insira um número: '))
    lista.append(num)

for i in lista:
    if i % 2 == 0:
        par += 1
    else:
        impar +=1

print(f'Tem {par} números pares e {impar} números impares')