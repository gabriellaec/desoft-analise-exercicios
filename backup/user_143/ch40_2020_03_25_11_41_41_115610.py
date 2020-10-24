def soma_valores(s):
    i=0
    y=s[i]
    while(i<len(s)):
        y+=s[i+1]
        i+=1
    return y