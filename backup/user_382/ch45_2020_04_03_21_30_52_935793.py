lista = []
while True:
    num = int(input())
    if num <= 0:
        break
    else: 
        lista.append(num)
print(lista[::-1])