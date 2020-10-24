def soma_impares(n):
    num=len(n)
    i=0
    soma=0
    while i<len(n):
        if len(i)%2!=0:
            soma+=n[i]
            i+=1
print(soma)
        
            