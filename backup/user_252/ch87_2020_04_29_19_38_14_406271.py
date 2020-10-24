with open('churras.txt', 'r') as arquivo:
    comida=arquivo.readlines()
t=0
for i in comida:
    l=i.split(',')
    x=float(l[1])
    y=float(l[2])
    s=x*y
    t+=s
print(t)
    
    
    
    
    
    