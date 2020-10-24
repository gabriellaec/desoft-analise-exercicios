def bairro_mais_custoso(dicionario):
    dicionarionovo = total_do_semestre_por_bairro(dict)
    maior = dicionarionovo[0][1]
    i = 0
    while i <= len(dicionarionovo):
        if dicionarionovo[i][1] > maior:
            maior = dicionarionovo[i][1]
        else:
            continue
    print(maior)