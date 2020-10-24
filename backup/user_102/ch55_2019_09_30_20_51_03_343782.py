def primos_entre(a,b):
    d =[]
    i = a
    d.append(a)
    while i < b:
        i +=1
        if i % 2 != 0:
            d.append(i)
    return d