def verifica_primos(lista):
    u= len(lista)
    dicName={}
    dicName.update({})
    a=1
    for a in range(u):
        if a%2==0 and a!=2:
            dicName.update({a:False})
        if a%3==0 and a!=3:
            return dicName.update({a:False})
        if a%4==0 and a!=4:
            return dicName.update({a:False})
        if a%5==0 and a!=5:
            return dicName.update({a:False})
        if a%6==0 and a!=6:
            return dicName.update({a:False})
        if a%7==0 and a!=7:
            return dicName.update({a:False})
        if a%8==0 and a!=8:
            return dicName.update({a:False})
        if a%9==0 and a!=9:
            return dicName.update({a:False})
        else:
            return dicName.update({a:True})
    return dicName.update({})