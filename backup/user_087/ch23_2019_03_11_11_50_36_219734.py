def verifica_idade(x):
    If x < 18:
        print("Não está liberado")
    elif x > 21:
        print("Liberado EUA e BRASIL")
    else:
       print("Liberado BRASIL")
    
int(input('Qual a sua idade?'))