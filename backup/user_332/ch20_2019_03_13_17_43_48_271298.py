def saudar (NOME):
    if(NOME == "Chris"):
        return("Todo mundo odeia o Chris")
    else:
        return("Olá, {0}".format(NOME))
NOME = input("Qual eh seu nome?")
print(saudar(NOME))