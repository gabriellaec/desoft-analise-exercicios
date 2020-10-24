def soma_impares(x):
    t = 0
    for i in x:
        if x%2 != 0:
            t += i
    return(t)
    