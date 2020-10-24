def verifica_preco(nome, dicionome, diciocor):
    for i in dicionome:
        if nome==i:
            cor=dicionome[i]
            for e in diciocor:
                if cor==e:
                    return diciocor[e]