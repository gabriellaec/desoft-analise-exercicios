with open ('churras.txt') as lista:
    consumo=lista.read()
custos=0    
x=consumo.split(',')
for e in range (0,len(x)-2,3):
    custos+=consumo[e+1]*consumo[e+2]

print(custos)    


