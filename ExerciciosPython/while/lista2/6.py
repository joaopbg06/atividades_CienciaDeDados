# 6. Solicite ao usuário uma nota entre 0 e 10. Caso o valor seja inválido, peça novamente até
# que o usuário informe um valor válido.


while True:
    num = int(input('Insira uma nota entre 0 & 10: '))

    if num <= 10 and num >= 0:
        print("Nota valida")
        break
    
