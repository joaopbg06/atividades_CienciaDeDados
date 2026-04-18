# 8. Encontrando o maior número inserido pelo usuário. Peça números ao
# usuário e, ao digitar 0, exiba o maior número inserido.

num = int(input("Insira um número: "))
lista = []

while num != 0:
    lista.append(num)
    num = int(input("Insira um número: "))


print(max(lista))