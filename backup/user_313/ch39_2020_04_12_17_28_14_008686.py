termos = []
for n in range(1,999):
    conta  = 0
    lista = [0]
    lista[0] = n

    while True:
        if n % 2 == 0:
            n = n/2
            lista.append(n)
            if n == 1:
                break
            
        else: 
            n = n*3+1
            lista.append(n)
            if n == 1:
                break
    
    termos.append(len(lista))    
    #print('Collatz para numero {} gerou uma sequencia com {}'.format(lista[0],len(lista)))
for i in range(0,len(termos)):
    a = max(termos)
    if termos[i] == a:
        #print ('O numero que gerou a maior sequencia foi {} com uma sequencia de {}'.format(i+1,a))
        print(i+1)