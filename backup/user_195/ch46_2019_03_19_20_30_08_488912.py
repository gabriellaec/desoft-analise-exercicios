palavra=input("Fale uma palavra")
L=[]
while palavra!="fim":
    L.append(palavra)
    palavra=input("Fale outra palavra")
i=0
while i<len(L):
    if L[i][0]=="a":
        print(L[i])
    i+=1
