def capitaliza(palavra):
    maiusculas=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    minusculas=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    pal=[]
    for i in palavra:
        pal.append(i)
        
    for i in range(len(minusculas)):
        if pal[0] == minusculas[i]:
            pal[0] = maiusculas[i]
    string=" " 
    for i in range(len(pal)):
        string+=pal[i]
    return string
print(capitaliza("enzo"))


    