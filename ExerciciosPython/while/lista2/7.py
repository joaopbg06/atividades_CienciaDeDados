# 7. Considere dois países: A com 80.000 habitantes e taxa de crescimento anual de 3%, e B
# com 200.000 habitantes e taxa de 1,5%. Determine quantos anos serão necessários para
# que a população do país A ultrapasse a população do país B. 
A = 80000
B = 200000
anos = 0

while True:
    anos += 1

    A *= 1.03
    B *= 1.015

    if A >= B:
        print(f"Vai demorar {anos} anos para o país A ultrapassar")
        break