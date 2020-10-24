def monta_mala(pesagem):
    resultado=[]
    w=0
    for i in range (len(pesagem)):
        w+=pesagem[i]
        if w>23:
            break
        resultado.append(pesagem[i])
    retur resultado

testado=[10,12,1,5]
print(monta_mala(testando))