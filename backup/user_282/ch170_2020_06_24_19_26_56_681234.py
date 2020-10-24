def apaga_repetidos(str):
    lista = []
    newStr = ""
    for i in str:
        if i in lista:
            newStr += '*'
        #elif i.upper() in lista:
           # newStr += '*'
        else: 
            newStr += i
            lista.append(i)
    return newStr