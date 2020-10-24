with open ('churras.txt', 'r') as  arquivo:
    cont=arquivo.read()
l=cont.split('
')
v=0
for i in l:
    li=i.split(',')
    float(li[1])
    float(li[2])    
    v+=li[1]*li[2]
print(v)
    
    