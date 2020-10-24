vazia = []
perg = input("Digite as palavra: ")
i = 0
while perg != "fim":
    perg = perg[i]
    if perg[0] == "a":
        vazia.append(perg[0])
    i+=1
print(vazia)
    
        