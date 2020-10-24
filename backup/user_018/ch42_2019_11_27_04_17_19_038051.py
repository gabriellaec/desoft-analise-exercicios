n =10371784981

def quantos_uns(n):
    a=str(n)
    i=0
    num=0
    while i < len(a):
        if a[i] == '1':
            num+=1
        i+=1
    return num

print(quantos_uns(n))