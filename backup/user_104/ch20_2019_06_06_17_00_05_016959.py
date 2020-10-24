nome = input('Qual é seu nome?')
def fala_nome(nome):
    if nome == 'Chris':
        x = 'Todo mundo odeia o Chris'
    else:
        x = 'Olá, {}'.format(nome)
    return x
print(fala_nome(nome))