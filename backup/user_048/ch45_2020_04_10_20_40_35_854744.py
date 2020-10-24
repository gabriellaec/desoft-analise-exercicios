lista=[]
pergunta=True
while pergunta:
    r=int(input("digite numero"))
    if r==0 or 0>r :
        pergunta=False
    else:
        lista.append(r)
for i in reversed(lista):
    print(i)
        
    