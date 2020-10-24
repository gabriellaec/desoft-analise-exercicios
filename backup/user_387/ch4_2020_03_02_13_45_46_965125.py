def classifica_idade(x):
    if x <= 11:
        return(str('crianca'))

    elif x <= 17:
        return(str('adolescente'))

    else: 
        return(str('adulto'))

x = float(input("Qual sua idade: "))

c = classifica_idade(x)

print(c)
