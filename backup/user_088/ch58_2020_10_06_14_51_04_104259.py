def conta_a(string):
    i=0   
    vezes=0
    lista=[0]*len(string)
    while(i<len(string)):
        if(lista[i]=="a"):
            vezes+=lista[i]
        i+=1     
    return string
        
   