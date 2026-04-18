# 9. Contar quantos números pares o usuário digitar. O programa deve
# contar quantos números pares o usuário inseriu. O usuário para
# digitando -1.


num = int(input("Insira um número: "))
cont = 0

while num != -1:
    if num % 2 == 0:
        cont += 1
    num = int(input("Insira um número: "))


print(f"Você digitou {cont} números pares")