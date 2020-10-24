def soma_valores(s):
    i=0
    y=s[i]
    for i in range (len(s)):
        y+=s[i+1]
    return y