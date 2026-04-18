# 14. Faça um programa que peça uma nota, entre zero e dez. Mostre uma
# mensagem caso o valor seja inválido e continue pedindo até que o usuário
# informe um valor válido.


for tentativa in range(100):  
    nota = float(input("Insira uma nota entre 0 e 10: "))
    

    if 0 <= nota <= 10:
        print(f"Nota válida: {nota}")
        break
    else:
        print("Nota inválida! A nota deve estar entre 0 e 10.")
else:

    print("Número máximo de tentativas atingido.")
