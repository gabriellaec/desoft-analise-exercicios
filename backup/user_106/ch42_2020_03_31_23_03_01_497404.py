lista=[]

while True:
    t=input('Digite uma palavra: ')
    if t=='fim':
        break
    lista.append(t)
    
i=0
    
while i<len(lista):
    if lista[i][0]=='a':
        print (lista[i])
    i+=1