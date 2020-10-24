def funcao(a,c):
    t=(c*365*a*10)/1536
    return t
    #t=(c*10*30*12*a)/1440
a=int(input('cigarro dia: '))
c=int(input('anos: '))
q=funcao(a,c)
print (q)