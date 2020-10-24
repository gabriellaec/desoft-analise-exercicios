custo=0
with open( 'churras.txt','r' ) as arquivo:
    a=arquivo.readlines()
    lista.append(a)
    for e in a:
        b=e.split(",")
        c=float(b[1])
        d=float(b[2])
        custo+=c*d
        
print(custo)
        
    