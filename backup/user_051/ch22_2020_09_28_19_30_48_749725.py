def funcao():
    c=float(input('quantos cigarros vc fuma por dia? '))
    a=float(input('hรก quantos anos vc fuma? '))
    if c==0 or a==0:
        return 0
    t=(c*365*a*10)/10
    #t=(c*10*30*12*a)/1536
    return t
print (funcao())