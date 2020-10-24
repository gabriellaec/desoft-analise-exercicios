def verifica_idade(a):
    if a<18:
        return "Não está liberado"
    elif a>=18 and a<21:
        return "Liberado BRASIL"
    elif a>=21:
        return "Liberado EUA e BRASIL"
    
print (verifica_idade(18))