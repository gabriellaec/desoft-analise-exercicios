lista=[]
b=input('digite uma palavra')
while b!='fim':
    lista.append(b)
    b=input('digite uma palavra')
i=0
while i<len(lista):
    b=lista[i]
    if len(b)> 1 and b[0]=="a":
    	print (b)
    i+=1


    
    
