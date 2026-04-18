# 7. Adivinhe o número secreto (de 1 a 10). O usuário deve tentar adivinhar
# um número até acertar. (Declare um valor e receba outro)


x = int(input('Insira o número secreto: '))

while x != 6:
    print("ERROU!!!")
    x = int(input('Insira o número secreto: '))
print("ACERTOU!!!")