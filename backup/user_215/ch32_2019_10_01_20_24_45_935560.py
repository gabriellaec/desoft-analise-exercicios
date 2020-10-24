duvida = "sim"

while duvida != "não":
    duvida = str(input("Voce está com duvidas? "))
    if duvida != "não":
        print("Pratique mais")
    else: 
        print("Até a próxima")