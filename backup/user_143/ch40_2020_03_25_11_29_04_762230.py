def soma_valores(s, i):
    y[0]=s[0]
    while(i<=s):
        y[i+1]+=s[i+1]
        i+=1
    return y