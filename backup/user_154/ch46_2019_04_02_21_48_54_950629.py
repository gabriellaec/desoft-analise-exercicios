lista = []

while True:
    string = input("Digite sua palavra: ")
    
    if string == "fim":
        break
    else:
        lista.append(string)

result = []

for x in lista:
    if x[0] == "a":
        result.append(x)

print(result)