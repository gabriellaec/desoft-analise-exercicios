l=input('insira sua lista')
def classifica_lista(l):
    i=1
    t=[]
    while i<=len(l):
        if l[i]>l[i-1]:
            t.append(1)
        elif l[i]>l[i-1]:
            t.append(-1)
    cd=len(t)
    if cd==sum(t):
        print("crescente")
    elif cd== (sum(t))*(-1):
        print("decrescente")
    else:
        print('nada')