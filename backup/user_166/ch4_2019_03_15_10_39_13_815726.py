i= int(input("qual sua idade?"))
def classifica_idade(i):
    if i<=11:
        print ("crianca")
    elif 12<=i<=17:
        print ("adolescente")
    else:
        print ("adulto")