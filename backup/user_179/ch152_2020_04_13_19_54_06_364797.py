def verifica_preco (nome,dicionario_cores,dicionario_precos):
        cor = dicionario_cores.get(nome)
        preco = dicionario_precos[cor]
        return preco