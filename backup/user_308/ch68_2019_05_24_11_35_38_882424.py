def separa_trios(lista):
    cont=0
    i=0
    for e in range(1,len(lista)+1):
        trio=[]
        trio.append(lista[e])
        if e%3==0:
            print(trio)
            trio=[]