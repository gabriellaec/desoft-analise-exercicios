lista=[10,20,30,40]

def soma_valores(elementos):
    i=0
    s=0
    while i<len(elementos):
        s+=elementos[i]
        i+=1
    return s

print(soma_valores(lista))
        