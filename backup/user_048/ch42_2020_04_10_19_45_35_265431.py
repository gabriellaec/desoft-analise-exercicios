pergunta=True
lista=[]
listad=[]
while pergunta:
    p=input("Digite uma palavra")
    if p=="fim":
        pergunta=False    
    else:
        lista.append(p)
for n in lista:
    g=n.startswith("a")
    if g:
        listad.append(n)
       
    