with open('churras.txt', "r") as file:
    y=file.read()
i=0
lista=[]
while i<len(y)/3:
    p=y[1+3*i]
    print(p)
    q=y[2+3*i]
    print(q)
    v=p*q
    print(v)
    lista.append(v)
    i+=1
print(sum(lista)) 