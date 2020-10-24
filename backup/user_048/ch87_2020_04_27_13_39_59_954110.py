with open('churras.txt', "r") as file:
    y=file.read()
w=y.split(",")
i=0
lista=[]
while i<len(w)/3:
    p=w[2+3*i]
    print(p)
    q=w[1+3*i]
    print(q)
    v=p*q
    lista.append(v)
    i+=1
print(sum(lista)) 