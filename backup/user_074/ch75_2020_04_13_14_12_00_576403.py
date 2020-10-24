def verifica_primos(lista):
    u= len(lista)
    dicName.update({})
    a=1
    for a in range(u):
        if a%2==0 and a!=2:
            dicName.update({a:False})
            return False
        if a%3==0 and a!=3:
            dicName.update({a:False})
            return False
        if a%4==0 and a!=4:
            dicName.update({a:False})
            return False
        if a%5==0 and a!=5:
            dicName.update({a:False})
            return False
        if a%6==0 and a!=6:
            dicName.update({a:False})
            return False
        if a%7==0 and a!=7:
            dicName.update({a:False})
            return False
        if a%8==0 and a!=8:
            dicName.update({a:False})
            return False
        if a%9==0 and a!=9:
            dicName.update({a:False})
            return False
        else:
            dicName.update({a:True})
            return True
    return dicName.update({})