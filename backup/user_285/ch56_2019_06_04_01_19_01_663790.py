def calcula_total_da_nota(precos,quantias):
    nota=0
    for i in range(len(precos)):
        precoporproduto=precos[i]*quantias[i]
        nota+=precoporproduto
    return nota
            
    