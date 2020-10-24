#Programa que odeia o Chris
def odeia_o_chris(nome):
    x = input('Qual o seu nome?')
    if nome == 'Chris':
        print('Todo mundo odeia o Chris')
    else:
        print('Olá,' .format(x))
