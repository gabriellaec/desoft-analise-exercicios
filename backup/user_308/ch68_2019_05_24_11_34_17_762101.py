def separa_trios(lista):
    cont=0
    i=0
    for e in range(len(lista)):
        trio=[]
        trio.append(lista[e])
        if e%3==0:
            print(trio)
            trio=[]