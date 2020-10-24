NOME = input("Qual é seu nome?: ")

def nome(NOME):
    if NOME != "Chris":
        return "Olá, {0}".format(NOME)
    else:
        return "Todo mundo odeia o Chris"
    
print(nome(NOME))


