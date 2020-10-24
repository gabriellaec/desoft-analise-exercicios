def classifica_idade(i):
    resposta = input("Qual sua idade?")
    if resposta <= 11: 
        return "crianca"
    elif 12 <= i and i <= 17:
        return "adolescente"
    else: 
        return "adulto"