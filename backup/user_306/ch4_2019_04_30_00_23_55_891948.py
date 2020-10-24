def classifica_idade(x):
    if x <= 11:
        print("crianca")
    elif x >= 12 or x <= 17:
        print("adolescente")
    else:
        print("adulto")
        
x = int(input("Qual a sua idade?"))