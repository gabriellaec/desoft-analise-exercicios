perg = input("Digite as palavra: ")
vazia = []
while perg!= "fim":
    if perg[0] == "a":
        vazia.append(perg)
    perg = input("Digite as palavra: ")
i = 0
while i < len(vazia):
    print(vazia[i])
    i+=1
    

    
        