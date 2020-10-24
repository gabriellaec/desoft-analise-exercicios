def monta_mala(a, b):
    a=[]
    b=int(input('Qual o peso?: '))
    a.append(b)
    while sum(a)<=23:
        b=int(input('Qual o peso?: '))
        a.append(b)
        print (a)