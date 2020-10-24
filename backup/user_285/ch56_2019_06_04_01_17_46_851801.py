def calcula_total_da_nota(precos,quantias):
    nota=0
    for i in range(len(precos)):
        for e in range(len(quantias)):
            precoporproduto=precos[i]*quantias[e]
            nota+=precoporproduto
    return nota
            
    