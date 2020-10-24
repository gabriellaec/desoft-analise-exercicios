def verifica_primos(x):
    dict={}
    i=0
    x[i]=int(x[i])
    while i<len(x):
        divisor=2
        primo=true
        if x[i]<2:
            dict[x[i]]=false
        elif x[i]==2:
            dict[x[i]]=True
        else:
            while divisor<x[i]:
                if x[i]*divisor==0
                primo=false
                divisor+=1
            dict[x[i]]=primo
        i+=1
    return dict