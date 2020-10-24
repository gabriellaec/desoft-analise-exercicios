def classifica_idade(anos):  
    x = input("age: ")
    if x<11:
        return "crianca"
    if 12<x<17:
        return "adolescente"
    if x>18:
        return "adulto"