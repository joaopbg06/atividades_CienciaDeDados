# 8. Implemente um sistema de caixa registradora onde o usuário insere valores dos produtos.
# A entrada de 0 indica o fim da compra. Exiba o total da compra, peça o valor pago e exiba
# o troco. Após isso, o programa deve reiniciar para um novo cliente.
total = 0

print("============ CARDÁPIO ============")
print("1. Hambúrguer .......... R$ 15,00")
print("2. Pizza ............... R$ 25,00")
print("3. Refrigerante ........ R$ 5,00")
print("==================================")
print('')

while True:
    pedido = int(input('Insira o número do prato para comprar (digite 0 para finalizar): '))

    match pedido:
        case 1:
            total += 15
            print('Hambúrguer adicionado ao pedido')
        case 2:
            total += 25
            print('Pizza adicionado ao pedido')
        case 3:
            total += 5
            print('Refrigerante adicionado ao pedido')
        case 0:
            print(f"O total da compra foi de R${total:0.2f}")
            pagamento = int(input('Insira o valor para realizar o pagamento: '))

            if pagamento < total:
                print(f"Faltou pagar R${total - pagamento:0.2f}")
            elif pagamento > total:
                print(f"O troco ficou em R${pagamento - total:0.2f}")
            else: 
                print("Compra realizada com sucesso")
            break
        case _:
            print('Valor Indefinido')