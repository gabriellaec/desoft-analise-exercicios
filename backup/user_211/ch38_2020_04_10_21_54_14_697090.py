def quantos_uns(n):
    #str transforma o número numa string(tudo juntinho, tipo 12341
    #o map faz todos os elementos dessa string se transformarem em inteiros
    #A principal diferença entre strings e listas em Python é que strings são imutáveis, enquanto listas são mutáveis
    #Por fim list separa cada elemento desse número,tipo[1,2,3,4,1]
    res = list(map(int, str(n)))
    x=0
    i=0
    while i<len(res):
        if res[i]==1:
            x=x+1
        i=i+1
    print(res)
    return x
print(quantos_uns(1648126418296))