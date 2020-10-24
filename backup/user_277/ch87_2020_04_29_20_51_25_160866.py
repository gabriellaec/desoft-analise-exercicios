with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    h=conteudo.split(',')
    f=h.split('\n')
k=0
for i in range(0,len(f)):
    if i%3==0:
        k+=1
    elif i%3==2:
        k=0
    else:
        s=h[i]*h[i+1]
print (s)
        
       