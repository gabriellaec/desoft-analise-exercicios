def capitaliza(numero):
    minuscula=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    maiuscula=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    while i < len(minuscula):
        if minuscula[i]==numero[0]:
            numero[0]=maiuscula[i]
        else:
            i+=1
    
    