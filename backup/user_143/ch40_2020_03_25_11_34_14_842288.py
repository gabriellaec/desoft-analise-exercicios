def soma_valores(s):
    i=0
    y[i]=s[i]
    while(i<=len(s)):
        y[i+1]+=s[i+1]
        i+=1
    return y