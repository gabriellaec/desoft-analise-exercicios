n =10371784981

def quantos_uns(n):
    a=str(n)
    i=0
    uns=0
    while i < len(a):
        if a[i] == '1':
            uns+=1
        i+=1
    return uns

print(quantos_uns(n))