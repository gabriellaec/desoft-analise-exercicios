def capitaliza(palavra):
    maiusculas=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    minusculas=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(len(minusculas)):
        if palavra[0] == minusculas[i]:
            i=posicao
    palavra[0]=maiusculas[posicao]
    return palavra

def capitaliza(palavra):
    i=minusculas.indexOf(palavra[0])
    maiusculas[i]