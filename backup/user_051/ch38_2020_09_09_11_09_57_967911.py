def quantos_uns(x):
    i=0
    for a in x:
        if a=='1':
           i+=1
    return i
print (quantos_uns(str(1112)))