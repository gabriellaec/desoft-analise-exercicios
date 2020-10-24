LISTA=[]
NUM=int(input('número?'))
while NUM>0:
    LISTA.append(NUM)
    NUM = int(input('número?'))
i=len(LISTA) - 1
while i>=0:
    print(LISTA[i])
    i-=1