i=2
d=1
a=0
while i<=1000 and d<=1000:
    lista=[]
    c(i)=len(lista)
    while i!=1:
        if i%2==0:
            i=i/2
            lista.append(i)
        else:
            i=(3*i)+1
            lista.append(i)
    if c(i)>c(i+d):
        d+=1
        a+=1
        if a==999:
            print ("o número é {0}". format(lista[0])
            i=1001
    else:
        i+=1