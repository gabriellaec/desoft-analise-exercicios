import random
n1=random.radint()
n2=random.radint()
n3=random.radint()
def classifica_lista(n1,n2,n3):
    if n1<n2<n3:
        print ('crescente')
    elif n1>n2>n3:
        print ('decrescente')
    else:
        print ('nenhum')