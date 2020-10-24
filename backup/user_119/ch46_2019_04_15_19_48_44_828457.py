palavra=str(input('palavra? '))
lista=[]
while palavra!='fim':
    lista.append(palavra)
    palavra=str(input('palavra? '))
i=0
while i<len(lista):
    palavra=lista[i]
    if palavra[0]=='a':
    	print (palavra)
    i+=1
    