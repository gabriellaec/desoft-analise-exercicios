def verifica_primos(lista):
    u= len(lista)
    dicName={}
    a=-2
    for lista[a] in range(u):
        a+=1
        if lista[a]%2==0 and lista[a]!=2:
            return dicName.update({lista[a]:False})
            dicName[a]
            print(a)
        if lista[a]%3==0 and lista[a]!=3:
            return dicName.update({lista[a]:False})
            dicName[a]
            print(a)
        if lista[a]%4==0 and lista[a]!=4:
            return dicName.update({lista[a]:False})
            dicName[a]
            print(a)
        if lista[a]%5==0 and lista[a]!=5:
            return dicName.update({lista[a]:False})
            dicName[a]
            print(a)
        if lista[a]%6==0 and lista[a]!=6:
            return dicName.update({lista[a]:False})
            dicName[a]
            print(a)
        if lista[a]%7==0 and lista[a]!=7:
            return dicName.update({a:False})
            dicName[a]
            print(a)
        if lista[a]%8==0 and lista[a]!=8:
            return dicName.update({lista[a]:False})
            dicName[a]
            print(a)
        if lista[a]%9==0 and lista[a]!=9:
            return dicName.update({lista[a]:False})
            dicName[a]
            print(a)
        else:
            return dicName.update({lista[a]:True})
            dicName[a]
            print(a)
        a+=1
    return dicName.update({})
    print(dicName)
