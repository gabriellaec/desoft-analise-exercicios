valor=0.00
with open ('churras.txt','r') as arquivo:
    l=[]
    l2=[]
    a=arquivo.read()
    colunas=a.split(',')
   	l.append(coluna[1])
    l2.append(coluna[2])
    i=-1
    for e in l:
        i+=1
        valor+=(e*l2[i])
print(valor)
        