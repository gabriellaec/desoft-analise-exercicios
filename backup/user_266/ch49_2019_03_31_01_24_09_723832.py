lista=[0]
i=0

while i<len(lista):
    n=int(input('Digite um número: '))
    if n>0:
        lista.append(n)
    else:
        break
    i+=1

i=0
inverso=lista[::-1]
inverso.pop()
while i<len(inverso):
    print(inverso[i])
    i+=1