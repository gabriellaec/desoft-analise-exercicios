nums = ['1','2','3','4','5','6','7','8','9']
lista_input_usuario = []
input_usuario = ''

def login_disponivel(lista_nome_lista):
    nome = lista_nome_lista[0]
    lista_nomes = lista_nome_lista[1]

    for name in lista_nomes:
        if name == nome:
            if nome[-1] not in nums:
                nome = str(nome) + str(1)
            elif nome[-1] in nums:
                nome = list(nome)
                nome[-1] = str(int(nome[-1]) + 1)
                nome = ''.join(nome)
    return nome

while True:
    input_usuario = input('Usuário digita: ')
    if input_usuario == 'fim':
        break
    l = [input_usuario, lista_input_usuario]
    lista_input_usuario.append(login_disponivel(l))

for nome in lista_input_usuario:
    print(nome)