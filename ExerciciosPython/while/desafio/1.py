# 1. Escreva um programa que leia um número N e imprima todos os termos da sequência de
# Fibonacci até que o maior termo seja menor ou igual a N.
# Exemplo:
#  Entrada: 20
#  Saída: 0 1 1 2 3 5 8 13
entrada = int(input('Insira um número: '))

x = 1
y = 0

while x <= entrada: 
    print(x)
    temp = x
    x = x + y
    y = temp
    
    