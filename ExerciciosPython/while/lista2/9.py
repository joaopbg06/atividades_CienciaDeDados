# 9. Implemente um sistema onde o usuário insere o código e a quantidade dos produtos
# desejados. O programa deve calcular o valor total e permitir que o usuário finalize o
# pedido digitando 0.

total = 0

print("=========== PRODUTOS ===========")
print("Código   Produto               Preço")
print("1010     Celular ............. R$ 1.200,00")
print("2020     Notebook ............ R$ 3.500,00")
print("3030     Fone de Ouvido ...... R$ 150,00")
print("================================")
print('')

while True:
    codigo = int(input("Insira o código do produto (Digite 0 para finalizar a compra): "))
    print('')
    if codigo != 0:
        quant = int(input("Insira a quantidade do  mesmo produto: "))

    match codigo:
        case 1010:
            total += quant * 1200
            print(f"{quant} Celular adicionado no carrinho")
        case 2020:
            total += quant * 3500
            print(f"{quant} Notebook adicionado no carrinho")
        case 3030:
            total += quant * 150
            print(f"{quant} Fone de Ouvido adicionado no carrinho")
        case 0:
            print(f"O total a ser pago é de R${total:0.2f}")
            break
        case _:
            print("valor invalido")