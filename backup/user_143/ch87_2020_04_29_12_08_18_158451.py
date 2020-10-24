with open ('churras.txt', 'r') as  arquivo:
    cont=arquivo.read()
l=cont.split('
')
for i in l:
    li=i.split(',')
print(li)
    