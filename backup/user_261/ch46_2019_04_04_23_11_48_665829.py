a=input("coloque as palavras:")
l=[]
while a!="fim":
    l.append(a)
    a=input("coloque as palavras:")
i=0
while i<len(l):
    if l[i][0]=="a":
        print(l[i])
    i+=1