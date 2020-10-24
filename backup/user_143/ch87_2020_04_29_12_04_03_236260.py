with open ('churras.txt', 'r') as  arquivo:
    cont=arquivo.read()
l=cont.split('\n')
print(l)
r=l.split(',')
i=0
while i<len(l):
    del(r[i])
    i+=3
for j in r:
    float(j)
a=0
b=0
v=0
while a<len(r):
    p=r[a]
    q=r[a+1]
    v+=p*q
    a+=2
print(v)
    