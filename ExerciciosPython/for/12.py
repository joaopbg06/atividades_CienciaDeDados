# 12. Numa eleição existem três candidatos. Faça um programa que peça o
# número total de eleitores. Peça para cada eleitor votar e ao final mostrar o
# número de votos de cada candidato.

total_eleitores = int(input("Digite o número total de eleitores: "))

votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

for i in range(1, total_eleitores + 1):
    print(f"\nEleitor {i}, vote no candidato:")
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    
    voto = int(input("Seu voto (1, 2 ou 3): "))
    
    # Contabilizar o voto
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    else:
        print("Voto inválido! Esse voto será ignorado.")  

# Mostrar o resultado da eleição
print("\nResultados da eleição:")
print(f"Candidato 1: {votos_candidato1} votos")
print(f"Candidato 2: {votos_candidato2} votos")
print(f"Candidato 3: {votos_candidato3} votos")
