
def calcula_total_da_nota (preco_produto,quantidade):
    preco_total = []
    i = 0
    while i < len(preco_produto):
        preco_total.append(preco_produto[i] * quantidade[i])
        i = i + 1
        
    return preco_total














