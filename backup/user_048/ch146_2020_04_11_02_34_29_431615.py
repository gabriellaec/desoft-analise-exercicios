from collections import Counter
#Counter({'abobora': 3, 'chuchu': 2})
def mais_frequente(lista):
    y=Counter(lista)
    v=y.values()
    m=max(v)
    for chave,valor in y.items():
        if valor ==m:
            return chave