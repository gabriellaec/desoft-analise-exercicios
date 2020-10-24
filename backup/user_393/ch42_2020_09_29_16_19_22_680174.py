lista= []
x= str
while True:
    x= input("Digite uma palavra:")
    lista.append(x)

    if x == 'fim':
        break
i= 0
palavras_que_comecam_com_a= []
while i < len(lista):
    if lista[i][0]== 'a':
        palavras_que_comecam_com_a.append(lista[i])
     
    i= i + 1
k= 0
while k < len(palavras_que_comecam_com_a):
    print(palavras_que_comecam_com_a[k])
    k= k + 1