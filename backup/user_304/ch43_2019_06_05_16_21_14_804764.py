i=2
while i<1000:
    i+=1
    sequencia=[]
    maior=0
    while i!=1:
        if i%2==0:
            i=i/2
            sequencia.append(i)
        else:
            i=3*i+1
            sequencia.appen(i)
    if len(sequencia)>maior:
        maior=len(sequencia)
return sequencia[0]
            
            
    