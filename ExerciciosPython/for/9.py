# 9. Faça um programa que peça um número inteiro e determine se ele é ou
# não um número primo. Um número primo é aquele que é divisível somente
# por ele mesmo e por 1.

num = int(input('Insira um número: '))
primo = True

loop = int(num ** 0.5 + 1)

for i in range(2, loop):
    if num % i == 0:
        primo = False
        break

if primo:
    print(f"{num} é primo.")
else:
    print(f"{num} não é primo.")