# 16. Faça um programa que receba a idade de 15 pessoas e que calcule e
# mostre:
# a) A quantidade de pessoas em cada faixa etária;
# b) A percentagem de pessoas na primeira e na última faixa etária, com
# relação ao total de pessoas:
#  Até 15 anos
#  De 16 a 30 anos
#  De 31 a 45 anos
#  De 46 a 60 anos
#  Acima de 61 anos

lista = []

faixa1 = 0 
faixa2 = 0 
faixa3 = 0  
faixa4 = 0  
faixa5 = 0  

for i in range(15):
    idade = int(input('Insira a idade: '))
    lista.append(idade)


for i in lista:

    if i <= 15:
        faixa1 += 1
    elif 16 <= i <= 30:
        faixa2 += 1
    elif 31 <= i <= 45:
        faixa3 += 1
    elif 46 <= i <= 60:
        faixa4 += 1
    else:
        faixa5 += 1

print(f"Tem {faixa1} até 15 anos  ||  corresponde a {(faixa1/15)*100:0.2f}%")
print(f"Tem {faixa2} entre 16 e 30 anos  ||  corresponde {(faixa2/15)*100:0.2f}%")
print(f"Tem {faixa3} entre 31 e 45 anos  ||  corresponde {(faixa3/15)*100:0.2f}%")
print(f"Tem {faixa4} entre 46 e 60  ||  corresponde {(faixa4/15)*100:0.2f}%")
print(f"Tem {faixa5} acima de 60 anos  ||  corresponde {(faixa5/15)*100:0.2f}%")