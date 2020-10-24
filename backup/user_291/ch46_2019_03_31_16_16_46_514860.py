palavra = []

Vdd = True

while Vdd:
    usuario = input("digite uma palavra: ")
    if usuario != "fim":
        palavra.append(usuario)
    else:
        Vdd = False

i = 0 
e = 0
while i < len(palavra):
    x = palavra[i]
    if x[e] == "a":
        print(x)
    i += 1
    
        