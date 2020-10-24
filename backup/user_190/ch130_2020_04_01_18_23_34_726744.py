def monta_mala(b):
    a=[]
    a.append(b)
    while sum(a)<23:
        a.append(b)
        return a
x=int(input('Qual o peso?: '))
print (monta_mala(x))