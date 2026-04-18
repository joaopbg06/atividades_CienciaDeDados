# 3. Somar números até o usuário digitar 0. Peça números ao usuário e
# some-os até que ele digite 0.


num = int(input('Insira um número: '))
soma = 0

while num != 0:
    soma += num
    print("A soma é:", soma)
    num = int(input('Insira um número: '))
print('Soma Encerrada')