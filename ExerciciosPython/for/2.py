
# 2. Faça um programa que receba dois números inteiros e gere os números
# inteiros que estão no intervalo compreendido por eles.

num1 = int(input('Insira um número inteiro: '))
num2 = int(input('Insira um número inteiro: '))

x = 1

if num1 > num2:
    x = -1
    num1 -= 1
else: 
    num1 +=1

for i in range(num1,num2, x):
    print(i)