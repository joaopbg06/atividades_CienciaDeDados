# 5. Escreva um programa que leia um número inteiro positivo e determine se ele é um
# quadrado perfeito (ou seja, se existe um número inteiro x tal que x² = n).
# Exemplo:
#  Entrada: 49
#  Cálculo: 7 × 7 = 49
#  Saída: 49 é um quadrado perfeito


entrada = int(input('Insira um número: '))

raiz = entrada ** 0.5

if raiz % 1 == 0:
    print('Este número é um quadrado perfeito')
else:
    print('Este número NÃO é um quadrado perfeito')
