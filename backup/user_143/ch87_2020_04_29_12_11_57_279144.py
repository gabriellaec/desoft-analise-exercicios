with open ('churras.txt', 'r') as  arquivo:
    cont=arquivo.read()
l=cont.split('\n')
v=0
for i in l:
    li=i.split(',')
    v+=li[1]*li[2]
print(v)
    
    