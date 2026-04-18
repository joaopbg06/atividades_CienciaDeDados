# 5. Solicite ao usuário números indefinidamente. O programa deve parar quando o usuário
# digitar um número igual ao anterior. Em seguida, exiba quantos números foram inseridos.

cont = 0
anterior = 0

while True:
    num = int(input('Insira um número: '))
    cont += 1
    
    if num == anterior:
        print(f'Foram inseridos {cont}° números')
        break

    anterior = num
    




