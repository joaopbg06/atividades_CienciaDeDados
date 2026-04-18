# 2. Solicite ao usuário que insira uma senha e continue pedindo até que ele insira a senha
# correta definida previamente.

senha = '1234'

while True:
    num = input('Insira a senha: ')
    if num == senha:
        print("Senha correta")
        break
    
