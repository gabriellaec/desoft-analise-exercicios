def calcula_total_da_nota(lista_p, lista_q):
    preco_final=0
    for i in range(0, len(lista_p)):
        preco_final+=lista_p[i]*lista_q[i]
    return preco_final