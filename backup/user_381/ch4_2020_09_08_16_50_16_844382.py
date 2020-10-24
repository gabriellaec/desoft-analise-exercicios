def classifica_idade(i):
    i = input("Qual sua idade?")
    if i <= 11: 
        print("crianca")
    elif 12 <= i and i <= 17:
        print("adolescente")
    else: 
        print("adulto")