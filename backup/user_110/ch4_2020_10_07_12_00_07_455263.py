def classifica_idade(idade):
    idade = int(input('qual a sua idade? '))
    if idade <= 11:
        print ("crianca")

    elif 12<= idade  <= 17:
        print ("adolescente")

    else:
        print ("adulto")