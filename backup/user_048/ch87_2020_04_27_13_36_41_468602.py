with open('churras.txt', "r") as file:
    y=file.read()
i=0
lista=[]
while i<len(y)/3:
    p=y[1+3*i]
    q=y[2+3*i]
    v=p*q
    lista.append(v)
print(sum(lista)) 