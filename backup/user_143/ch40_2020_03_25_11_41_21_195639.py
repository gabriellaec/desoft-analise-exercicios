def soma_valores(s):
    i=0
    y=s[i]
    while(i<=len(s)-2):
        y+=s[i+1]
        i+=1
    return y