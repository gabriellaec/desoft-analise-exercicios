with open ('churras.txt', 'r') as  arquivo:
    cont=arquivo.read()
l=cont.split(',')
i=0
while i<len(l):
    del(l[i])
    i+=3
for j in l:
    float(j)
a=0
b=0
v=0
while a<len(l):
    p=l[a]
    q=l[a+1]
    v+=p*q
    a+=2
print(v)
    