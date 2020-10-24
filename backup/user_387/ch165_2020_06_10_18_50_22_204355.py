def mais_populoso(br):
    dic = {}
    mais_pop = ''
    pop = 0
    for estado in br: 
        dic[estado] = 0
        for cidade in br[estado]:
            dic[estado] += br[estado][cidade]

    for estado in dic:
        if dic[estado] > pop:
            pop = dic[estado]
            mais_pop = estado
    return mais_pop