lista = []

while True:
    string = input("Digite sua palavra: ")
    
    if string == "fim":
        break
    elif string[0] == "a":
        lista.append(string)

for x in lista:
    print(x)