a= []
b= []
def calcula_total_da_nota(a,b):
    i= 0 
    c = []
    while i < len (a) and i < len(b):
        k = a[i] * b[i]
        c.append(k)
        i+=1
    return c