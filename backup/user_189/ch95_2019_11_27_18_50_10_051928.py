def mais_populoso(dic):
    pop = []
    pops = []
    estados = []

    for a in dic.values():
        for b in a.values():
            pop.append(b)
    i=0    
    while i< (len(pop)-1):
        soma = pop[i] + pop[i+1]
        pops.append(soma)
        i+=2

    nome_estados = dic.keys()

    for a in nome_estados:
        estados.append(a)

    maxpop = max(pops)
    print("pops", pops)
    for i in range(len(pops)):
        if pops[i] == maxpop:
            
            return "O estado mais populoso é: ",estados[i]


print(mais_populoso(brasil))    