with open ('churras.txt', 'r') as  arquivo:
    cont=arquivo.read()
l=cont.split('\n')
v=0
for i in l:
    li=i.split(',')
    o=float(li[1])
    o1=float(li[2])    
    v+=o*o1
print(v)
    
    