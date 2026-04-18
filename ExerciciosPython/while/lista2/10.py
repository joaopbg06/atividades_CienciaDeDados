# 10. Implemente um sistema de votação onde o usuário pode votar em candidatos (1 a 4), nulo
# (5) ou branco (6). O programa deve exibir o total de votos de cada tipo e a porcentagem de
# votos nulos e brancos. A entrada 0 encerra a votação.

print("=========== VOTAÇÃO ===========")
print("1        John Lennon")
print("2        Ozzy Osbourne")
print("3        Zé do bar")
print("4        Serj Tankian(cara do System of a down)")
print("5        Voto Nulo")
print("6        Voto em Branco")
print("0        Finalizar Votação")
print("===============================")
print('')

canditato1 = 0
canditato2 = 0
canditato3 = 0
canditato4 = 0
nulo = 0
branco = 0
total = 0

while True:
    voto = int(input("Insira seu voto: "))


    match voto:
        case 1:
            canditato1 += 1
            total += 1
            print('Voto registrado')
        case 2:
            canditato2 += 1
            total += 1
            print('Voto registrado')
        case 3:
            canditato3 += 1
            total += 1
            print('Voto registrado')
        case 4:
            canditato4 += 1
            total += 1
            print('Voto registrado')
        case 5:
            nulo += 1
            total += 1
            print('Voto registrado')
        case 6:
            branco += 1
            total += 1
            print('Voto registrado')
        case 0:
            
            
            
            print("")
            print("======================== VOTAÇÃO =========================")
            print(f"1        John Lennon                                      {canditato1}")
            print(f"2        Ozzy Osbourne                                    {canditato2}")
            print(f"3        Zé do bar                                        {canditato3}")
            print(f"4        Serj Tankian(cara do System of a down)           {canditato4}")
            print(f"5        Voto Nulo                                        {(nulo / total) * 100:0.1f}%")
            print(f"6        Voto em Branco                                   {(branco / total) * 100:0.1f}%")
            print("==========================================================")
            print("")
            
            break


        case _:
            print('Voto Invalido')