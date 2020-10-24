def classifica_idade (x,crianca,adolescente,adulto):
    if x<=11:
        return crianca;
    elif 12<=x<=17:
        return adolescente;
    else:
        return adulto;
    
x = int(input("qual a sua idade? "))
print (classifica_idade(x))
