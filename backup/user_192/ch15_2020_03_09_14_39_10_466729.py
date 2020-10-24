nome = input('Qual seu nome ')

def ola_nome (nome):
    if nome == 'Chris':
        return 'Todo mundo odeia o Chris'
    else:
        return 'Olá, {0}'.format(nome)

print(ola_nome(nome))

