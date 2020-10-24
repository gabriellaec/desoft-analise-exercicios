def qual_seu_nome(a):
    if a== 'Chris':
        return "Todo mundo odeia o Chris"
   
    else:
        return "Olá,{0}".format(a)

x=input("Qual seu nome? ")
print(qual_seu_nome(x))


