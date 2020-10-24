def verifica_progressao(x,y, z, o):
    i=0
    while i<len(lista):        
        if lista[i+1]-lista[i]==lista[i+2]-lista[i+1]:
            return A       
        elif lista[i+1]/lista[i]==lista[i+2]/lista[i+1]:
            return G
        elif lista[i+1]-lista[i]==lista[i+2]-lista[i+1] and lista[i+1]/lista[i]==lista[i+2]/lista[i+1]:
            return AG
        elif lista[i+1]-lista[i]!=lista[i+2]-lista[i+1] and lista[i+1]/lista[i]!=lista[i+2]/lista[i+1]:
            return NA
        i+=1
A="P.A"
G="P.G"
AG="A.G"
NA='N/A'

print(verifica_progressao(A,G, AG, NA))