# função que odeia o Chris
def everyone_hates_chris(name):
    if name == 'Chris' or name == 'chris':
        return 'Todo mundo odeia o Chris'
    else:
        return 'Olá, {}'.format(name)
    
 
a = input ('Insira seu nome: ')
c = everyone_hates_chris(a)
print(c)