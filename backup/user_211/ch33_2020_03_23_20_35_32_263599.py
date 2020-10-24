def primos_entre(a,b):
    primos = []
    x=a
    if a<=2:
        primos.append(2)
    while len(primos) < b:
        for i in range(2,x):
            if x % i == 0:
                break 
            if i == x-1:
                primos.append(x)
            x +=1
    return len(primos)
