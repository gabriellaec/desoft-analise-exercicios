palavras=[]
primeira_letra=[]
while True:
    p=str(input("Digite uma palavra e se não quiser colocar mais digite fim:"))
    palavras.append(p)
    primeira_letra.append(p[0])
    if p=="fim":
        break
print(palavras)
print(primeira_letra)
i=0
for i in range(len(palavras)):
    if primeira_letra[i]=="a":
        print(p[i])
        i+=1
    else:
        continue