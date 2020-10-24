with open("palavra.txt","r") as palavra:
    texto=palavra.read()

print(texto)

letras=0
for caracter in texto:
    if caracter in 'a':
        letras+=1
print (letras)