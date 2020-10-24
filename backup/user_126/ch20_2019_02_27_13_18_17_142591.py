def Todo_mundo_odeia_o_Chris(nomee):
    nome=str(nomee)
    if nome == 'Chris':
        return "Todo mundo odeia o Chris"
    else:
        return "Olá, "+nome
nome = input ('nome:')
print (Todo_mundo_odeia_o_Chris(nome))