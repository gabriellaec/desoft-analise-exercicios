def mais_populoso(dic):
    
    mais_populoso = 'a'
    maior_populacao = 0

    for estado in dic:

        soma = 0

        for cidade in dic[estado]:
            soma += dic[estado][cidade]

        if soma > maior_populacao:
            maior_populacao = soma
            mais_populoso = estado

    return mais_populoso