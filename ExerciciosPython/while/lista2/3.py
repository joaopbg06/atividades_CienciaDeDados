# 3. Peça ao usuário que insira notas (valores numéricos). A entrada deve continuar até que o
# usuário digite -1. Em seguida, exiba a média das notas.

soma = 0
cont = 0

while True:
    num = int(input('Insira a nota: '))

    if num == -1:
        print(f'A média é {soma / cont}')
        break

    cont += 1
    soma += num




