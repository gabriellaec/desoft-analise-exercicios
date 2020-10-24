def verifica_progressao(n)
i=0
x=n[i]-n[i+1]
y=n[i]/n[i+1]
while(i+2<len(n)):
    if(x==n[i+1]-n[i+2] and y==n[i+1]/n[i+2]):
        s="AG"
    if(x==n[i+1]-n[i+2]):
        s="PA"
    if(y==n[i+1]/n[i+2]):
        s="PG"
    else:
        s="NA"
return s