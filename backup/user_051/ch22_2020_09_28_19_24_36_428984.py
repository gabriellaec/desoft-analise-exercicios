def funcao(a,c):
    t=(c*10)*(365*a)/1536
    return t
    #t=(c*10*30*12*a)/1440
c=int(input('cigarro dia: '))
a=int(input('anos: '))
q=funcao(a,c)
print (q)