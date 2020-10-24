i=int(input('Qual sua idade? '))

def verifica_idade(a):
    if i<18:
        return "Não está liberado"
    elif i>=18 and i<21:
        return "Liberado BRASIL"
    elif i>=21:
        return "Liberado EUA e BRASIL"
    
print (verifica_idade(i))