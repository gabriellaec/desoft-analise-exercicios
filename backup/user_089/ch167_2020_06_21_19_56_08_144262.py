def bairro_mais_custoso(dicionario):
    dic2 = {}
    maior = 0 
    maior_bairro =""
    for k,v in dicionario.items():
        soma = 0       
        for e in v[6:]:
            soma += e
        dic2[k] = soma
    for k,v in dic2.items():
        if v > maior:
            maior_bairro = k
    return maior_bairro