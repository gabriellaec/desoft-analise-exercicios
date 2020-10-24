def soma_valores(s, i):
    i=0
    y=s[i]
    while(i<=10):
        y[i]+=s[i+1]
        i+=1
    return y