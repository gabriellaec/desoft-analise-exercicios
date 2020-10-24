def capitaliza(numero):
    minuscula=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    maiuscula=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    listanumero=[]
    numeronovo=''
    for i in numero:
        listanumero.append(i)
    for e in range(0,26):
        if minuscula[e]==listanumero[0]:
            listanumero[0]=maiuscula[e]
    for e in listanumero:
        numeronovo +=e
    return (numeronovo)