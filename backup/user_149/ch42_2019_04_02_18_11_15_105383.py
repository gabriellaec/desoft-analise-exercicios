def quantos_uns(x):
    i=0
    contagem=0
    while i<len(x):
        if x[i]=='1':
            contagem+=1
        i+=1
    print(contagem)