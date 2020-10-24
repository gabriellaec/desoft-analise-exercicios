l=[1,3,5,7,8]
def verifica_progressao(l):
    pa=True
    k=l[1]-l[0]
    for i in range(len(l)-1):
        if k!=(l[i+1]-l[i]):
            pa=False
    if pa==True:
        return "eh PA"

print(verifica_progressao(l))
            
