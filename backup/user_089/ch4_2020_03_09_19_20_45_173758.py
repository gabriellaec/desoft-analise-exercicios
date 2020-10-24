i=int(input("Qual sua idade?"))

def classifica_idade(i):

    if i <= 11:
        return('crianca')

    if i >= 12 or i <= 17 :
        return ("adolescente")

    else:
        return ("adulto")