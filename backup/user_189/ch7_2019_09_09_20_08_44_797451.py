vet=[]
def calcula_norma(vet):
    i=0
    for a in vet:
        if a == 1:
            break
        i+=1
    return i
        
print(calcula_norma(vet))
print(vet)    