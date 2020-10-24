x = list
def faixa_notas(x): 
    y = len(x)
    i = 0
    s1 = 0
    s2 = 0
    s3 = 0
    while i <= y:
        if x[i] < 5:
            s1 = s1 + 1
        if 5 <= x[i] <= 7:
            s2 = s2 + 1
        if x[i] > 7:
            s3 = s3 + 1
    Lista = [s1,s2,s3]
    return Lista