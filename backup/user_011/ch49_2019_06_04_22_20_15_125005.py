running = True
lista_num = []

while running:
    num = int(input('Digite um numero: '))
    if num > 0:
        lista_num.append(num)
    elif num <= 0:
        running = False
        
        
i = len(lista_num)
while i > 1:
    print(lista_num[i])
    i-=1
              