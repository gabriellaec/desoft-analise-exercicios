idade=int.input("qual e a sua idade)
def verifica_idade(idade):
    if idade >= 21:
        print("Liberado EUA e BRASIL") 
    elif idade < 21 and idade >= 18:
        print("Liberado BRASIL")
    else:
        print("Não está liberado")
        
