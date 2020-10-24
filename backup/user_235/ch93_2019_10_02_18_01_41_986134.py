def munch(x):
    lista=[int(a) for a in str(x)] 
    y=0
    soma=0
    while y < len(lista):
        soma+=lista[y]**lista[y]
        y+=1
    if soma==x:
        return True
    elif soma < 1 or soma != x:
        return False