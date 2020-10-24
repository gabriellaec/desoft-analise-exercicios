nome = input('Qual o seu nome? ')
if nome == 'Chris':
    resultado = 'Todo mundo odeia o Chris'
else:
    resultado = 'Olá, {}'.format(nome)
print(resultado)