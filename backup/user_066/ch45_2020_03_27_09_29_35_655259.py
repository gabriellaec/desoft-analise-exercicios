numeros = []
x = int(input())
while x > 0:
    numeros.append(x)
    x = input()
k = len(numeros)-1
while k >=0:
    print (numeros[k])
    k -= 1