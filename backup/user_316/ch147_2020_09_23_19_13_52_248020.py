def mais_frequente(l):
    resultado = {}
    for i in range(len(l)):
        print(" {0} {1}".format(l[i], l.count(l[i]))
        if i == 0 or l.count(l[i]) > resultado[l[i]]:
            resultado = dict(nome=l[i], contagem=int(l.count(l[i])))
    print("FINAL:  {0} {1}".format(l[i], l.count(l[i]))   
    return resultado.keys[0]