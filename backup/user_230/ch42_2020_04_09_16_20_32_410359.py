palavras=[]
while True:
    p=str(input("Digite uma palavra e se não quiser colocar mais digite "fim":"))
    palavras.append(p)
    if p=="fim":
        break
primeira_letra=p[0]
for i in palavras:
    if primeira_letra=="a":
        print (p)
    else:
        continue