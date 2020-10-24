def mais_populoso(dic):
    mp = 0
    for estado in dic:
        pop = 0
        for cidade in dic[estado]:
            pop += dic[estado][cidade]
        if pop > mp:
            mp = pop
            ep = estado
    return ep