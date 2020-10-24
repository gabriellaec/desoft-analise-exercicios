a=input('Palavra: ')
b=[]
while a!='fim':
    b.append(a)
    a=input('Palavra: ')
i=0

while i<(len(b)):
    c=(b[i])[0]
    if c=='a':
        print(b[i])
        i+=1
    else:
        i+=1
