with open ('churras.txt', 'r') as  arquivo:
    cont=arquivo.read()
l=cont.split('\n')
for i in l:
    li=i.split(',')
print(l)
    