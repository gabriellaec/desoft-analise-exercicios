palavra=input('Palavra: ')
lista=[]

while palavra!='fim':
    lista.append(palavra)
    palavra=input('Palavra: ')
i=0
while i<len(lista):
    palavra1=lista[i]
    if palavra1[0]=='a':
      print(palavra1)
    i+=1
	