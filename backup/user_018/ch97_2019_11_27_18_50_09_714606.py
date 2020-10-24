dic = {
    'bairro 1': [1234.45, 3245.45, 6125.32, 7654.34, 4829.45, 8193.32, 7034.78, 2845.3, 2920.34, 2984.6, 3916.75, 9843.89],
    'bairro 2': [2342.65, 3450.65, 8732.34, 6543.78, 1234.35, 2345.76, 4592.56, 9173.9, 2712.23, 4566.43, 5648.10, 3423.89 ]
}

def total_do_semestre_por_bairro(dic):
    soma = 0
	i=0
    copia = dic.copy()
    for k,lista in dic.items():
        while i < len((lista)-6):
            soma+=lista[i]
            i+=1
        copia.values() = soma

    return copia



print(total_do_semestre_por_bairro(dic))