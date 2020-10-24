a= []
b= []
def calcula_total_da_nota(a,b):
    i= 0 
    c = []
    while i < len (a+1) and i < len(b+1):
        c = a[i] * b[i]
        i+=1
    return c