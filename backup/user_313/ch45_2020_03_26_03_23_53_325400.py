lista=[]
a = True

while a:
    b = int(input('Digite um numero: '))
    if b > 0:
        lista.append(b)

    if b <= 0:
        a = False
        lista.reverse()
        print(lista) 
      