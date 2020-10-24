palavras=[]
while True:
    p=input("Digite uma palavra e se não quiser colocar mais digite fim:")
    palavras.append(p)
    if p=="fim":
        break
for i in range(len(palavras)):
    p=palavras[i]
    if p[0]=="a":
        print(p)