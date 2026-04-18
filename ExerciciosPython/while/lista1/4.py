# 4. O usuário deve digitar a senha correta (1234). Enquanto errar, o
# programa deve pedir novamente.


senha = '1234'
x = input('Insira a senha: ')


while x != senha:
    print('Senha incorreta')
    x = input('Insira novamente a senha: ')

print("senha correta")