# 1. Solicite ao usuário um número inteiro positivo e exiba apenas os números pares de 2 até
# esse número.


num = int(input('Insira um número: '))

while True:
    if num % 2 == 0:
        print(num)
    num = int(input('Insira um número: '))
    
