texto = ''

while texto != 'fim':
    texto = str(input('Escreva um usuário: '))
    print(login_disponivel(texto))