# 4. Solicite ao usuário que insira números. O programa deve continuar até que um número
# negativo seja inserido. No final, exiba o maior número informado.


maior = 0


while True:
    num = int(input('Insira um número: '))

    if num <= -1:
        print(f'O maior número é {maior}')
        break
    if num > maior:
        maior = num
