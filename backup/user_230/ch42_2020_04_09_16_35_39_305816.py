palavras=[]
primeira_letra=[]
while True:
    p=input("Digite uma palavra e se não quiser colocar mais digite fim:")
    palavras.append(p)
    primeira_letra.append(p[0])
    if p=="fim":
        break
print(palavras)
print(primeira_letra)
i=0
for i in range(0, len(primeira_letra)):
    if primeira_letra[i]=="a":
        print(p[i])
        i+=1
    else:
        continue