with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    h=conteudo.split(',','\n')
k=0
for i in range(0,len(h)):
    if i%3==0:
        k+=1
    elif i%3==2:
        k=0
    else:
        f=h[i]*h[i+1]
print (f)
        
       