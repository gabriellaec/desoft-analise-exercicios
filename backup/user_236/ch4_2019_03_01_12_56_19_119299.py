def classifica_idade (a):
    if a<=11:
        return ("crianca")
    elif 11<a<=17:
        return ("adolescente")
    else:
        return ("adulto")
    
a=int(input("qual a sua idade? "))

print (classifica_idade) 
