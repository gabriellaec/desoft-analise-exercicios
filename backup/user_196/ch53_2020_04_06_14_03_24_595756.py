a = []
def soma_impares(a):
    i=0
    while i < len(a):
        if a[i] % 2 != 0:
            a.append(i)
            i+=1
        else:
            i+=1
    return a

def soma_impares(a):
    for i in range (len(a)):
        if a[i] % 2 != 0:
            a.append(i)
        else:
            i+=1
    return a