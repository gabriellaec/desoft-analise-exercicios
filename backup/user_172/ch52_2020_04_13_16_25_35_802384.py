def calcula_total_da_nota(lista_p,lista_q):
    soma=0
    i=0
    while len(lista_p) > 0:
        valor = lista_p[i]*lista_q[i]
        soma = soma + valor
        i+=1
    return soma