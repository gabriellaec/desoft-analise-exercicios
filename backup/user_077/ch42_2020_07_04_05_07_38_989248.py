palavras=[]
a='oi'
while a!='fim':
    a=input('escreva uma palavra')
    palavras.append(a)
for p in palavras:
    if p[0]=='a':
        print(p)