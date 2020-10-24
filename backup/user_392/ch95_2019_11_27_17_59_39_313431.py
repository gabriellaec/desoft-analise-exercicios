def mais_populoso(x):
    maior = 0
    novo = 0
    for estado,dic in x.items():
        for cidade,pop in dic.items() :
            novo += pop
            if novo > maior:
                maior = novo
                return (estado)