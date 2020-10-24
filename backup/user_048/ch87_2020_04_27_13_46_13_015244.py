#ler texto e criar strings
with open('churras.txt', "r") as file:
    y=file.readlines()
#juntar listas em unica string
s=","
b=s.join(y)
#separar palavras pela virgula
w=b.split(",")
#loop
i=0
lista=[]
while i<len(w)/3:
    p=int(w[2+3*i])
    print(p)
    q=int(w[1+3*i])
    print(q)
    v=p*q
    lista.append(v)
    i+=1
print(sum(lista)) 