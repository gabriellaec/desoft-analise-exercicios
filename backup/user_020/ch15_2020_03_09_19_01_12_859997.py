#Programa que odeia o Chris
def odeia_o_chris(nome):
    if nome == 'Chris':
        print('Todo mundo odeia o Chris')
    else:
        print('Olá, '+nome)
x = input('Qual o seu nome?')
print(odeia_o_chris(x))
