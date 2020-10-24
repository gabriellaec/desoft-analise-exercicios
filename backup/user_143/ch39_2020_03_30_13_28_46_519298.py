i=2
lista=[]
while i<=1000:
    c(i)=len(lista)
    while i!=1:
        if i%2==0:
            i=i/2
            lista.append(i)
            else:
                i=(3*i)+1
                lista.append(i)
    if c(i)<c(i+1):
        i+=1
    else:
        print ("o número é {0}". format(lista[0])
        