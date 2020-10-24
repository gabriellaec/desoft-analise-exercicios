# função que odeia o Chris
def everyone_hates_chris(name):
    if name == 'Chris' or 'chris':
        return 'Todo mundo odeia o Chris'
    else:
        return name
    
 
a = input ('Olá, NOME')
c = everyone_hates_chris(a)
print(c)