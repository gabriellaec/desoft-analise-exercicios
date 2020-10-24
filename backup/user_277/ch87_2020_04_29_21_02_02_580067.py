with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    r=conteudo.replace('\n',',')
    h=r.split(',')

k=0
s=0
for i in range(0,len(h)):
    if i%3==0:
        k+=1
    elif i%3==2:
        k=0
    else:
        s+=h[i]*h[i+1]
print (s)
        
       