def verifica_idade(x):
    if x < 18:
        print("Não está liberado")
    elif x > 21:
        print("Liberado EUA e BRASIL")
    elif x <= 21 and x >= 18:
        print("Liberado BRASIL")
    
x= int(input('Qual a sua idade?'))