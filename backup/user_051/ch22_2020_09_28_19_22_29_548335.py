def funcao(a,c):
    t=(c*365*a*10)/1536
    return t
    #t=(c*10*30*12*a)/1440
c=int(input('cigarro dia: '))
if c<1:
    c+=1
a=int(input('anos: '))
if a <1:
    a+=1
q=funcao(a,c)
print (q)