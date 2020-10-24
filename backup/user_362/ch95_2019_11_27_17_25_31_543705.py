def mais_populoso(brasil): 
    dic={}
    for estado, cidade in brasil.items():
        #print(estado,cidade)
        #for local, pop in cidade.items():
        x=sum([int(pop)for pop in cidade.values()])
    print(x)
    dic[estado]=x
    
    mais_pop=0
    for estado, populacao in dic.items():
        if populacao>mais_pop:
            maior = estado
            mais_pop = populacao
    return maior
print (mais_populoso(brasil))