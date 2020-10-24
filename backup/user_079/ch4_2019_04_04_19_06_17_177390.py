def classifica_idade(anos):  
    x = input("age: ")
    if x<12:
        return "crianca"
    if 13<x<18:
        return "adolescente"
    if x>17:
        return "adulto"
    return x