lista=[]
a=int(input('Digite um numero: '))
while a!=0:
        lista.append(a)
        a=int(input('Digite um numero: '))
soma=[]  
soma=0     
i=0
while i<len(lista):
    soma+=lista[i]
    i+=1
print(soma)
      