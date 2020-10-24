vet=[]
def calcula_norma(vet):
    i=0
    for a in vet:
        i+=1
        if a == "1":
            return i
        
print(calcula_norma(vet))
print(vet)    