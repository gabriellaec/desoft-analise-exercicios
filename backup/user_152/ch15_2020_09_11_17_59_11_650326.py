def verifica_chris (name):
    if name != 'Chris':
        return 'Olá, {0}'.format(name)
    else:
        return 'Todo mundo odeia o Chris'

nome = input('Entre com o seu nome: ')
print(verifica_chris(nome))