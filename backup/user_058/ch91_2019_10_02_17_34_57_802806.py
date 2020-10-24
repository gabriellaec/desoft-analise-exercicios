with open("palavra.txt","r") as palavra:
    texto=palavra.read()

print(texto)

texto = texto.replace(" ","")
texto = texto.replace("\n","")
texto = texto.replace(".","")
texto = texto.replace("!","")
texto = texto.replace("?","")
texto = texto.replace(",","")
texto = texto.replace(";","")

letras=0
for caracter in texto:
    if caracter in 'a':
        letras+=1
print (letras)