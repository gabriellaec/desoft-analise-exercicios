
total = 0 

def calcula_total_da_nota(a,b):
    total = 0 
    for i in range(0,len(a)):
        total+= a[i]*b[i]
    return total 
        
    