def Chris(nome):
    if nome == 'Chris': 
        return 'Todo mundo odeia o Chris'
    else:
        return 'Olá, {0}'.format(nome)
nome = input('Qual seu nome?')
print(Chris(nome))
             
