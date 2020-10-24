def verifica_progressao (lista):
    r=lista[2]-lista[1]
    q=lista[2]/lista[1]
    if lista[3]*q==lista[4] and lista[3]+r==lista[4] and lista[-2]+r==lista[-1] and lista[-2]*q==lista[-1]:
        return 'AG'
    elif lista[3]*q==lista[4]  and lista[-2]*q==lista[-1]:
        return "PG"
    elif lista[3]+r==lista[4]  and lista[-2]+r==lista[-1]:
        return "PA"
    else return "NA"
    