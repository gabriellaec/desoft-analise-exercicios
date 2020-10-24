def monta_mala(pesos):
    result=[]
    x=0
    for i in range (len(pesos)):
        x+=pesos[i]
        if x>23:
            break
        result.append(pesos[i])
    return result
