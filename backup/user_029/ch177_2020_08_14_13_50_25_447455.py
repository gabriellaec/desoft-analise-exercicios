def numero_digitos(s):
    contador = 0 
    for i in s:
        if i.isdigit() == True:
            contador +=1
            print(i)
    return contador

            
        