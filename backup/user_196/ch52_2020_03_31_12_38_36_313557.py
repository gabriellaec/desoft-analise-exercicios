a= []
b= []
def calcula_total_da_nota(a,b):
    i= 0 
    c = []
    while i < len (a) and i < len(b):
        c = a[i] * b[i]
        i+=1
    return c