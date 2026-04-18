# 11. Faça um programa que peça para n pessoas a sua idade, ao final o
# programa deverá verificar se a média de idade da turma varia entre 0 e
# 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou
# idosa, conforme a média calculada.

turma = []
soma = 0

faixa = int(input("Insira a quantidade de pessoas na turma: "))

for i in range(faixa):
    idade = int(input(f"Insira a idade da {i}° pessoa: "))
    soma += idade
media = soma / faixa

if media <= 25:
    print("jovem")
elif 26 <= media <= 60:
    print("adulta") 
else:
    print("idosa")