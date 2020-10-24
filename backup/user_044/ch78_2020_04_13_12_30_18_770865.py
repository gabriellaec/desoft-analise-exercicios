import math
def calcula_tempo(dic):
    dn={}
    for i,n in dic.items():
        t=math.sqrt(200/n)
        dn[i]=t
    return dn
dic={}
x=0
while x!='sair':
    x=input("Qual o nome? ")
    if x!='sair':
        a=float(input("Qual é a acelerção? "))
    dic[x]=a
dn=calcula_tempo(dic)
s=10000
for i,n in dn.items():
    if n<s:
        s=n
        m=i
print('O vencedor é {0} com tempo de conclusão de {1} s'.format(m,s))


    