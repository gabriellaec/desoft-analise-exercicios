with open('churrasco.txt','r',encoding='utf-8') as arquivo:
    
    a=arquivo.readlines()

lista=[]   
for i in a :
    c=i.split(',')
    lista.append(c)

soma=0

for e in range(0,len(lista)):
        x=lista[e][1]
        y=lista[e][2]
        soma+=int(x)*float(y)



print(soma)



