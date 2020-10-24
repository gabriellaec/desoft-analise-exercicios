def eh_primo(num):
    t = 0 #contador 
    x = 0 #contador de index pra lista 
    n = int(input('Insira o valor de n:'))
    div = 3
    num = 0 #num a serem testados se eh primo ou nao 
    lista = [0]*n
    while n >= t:
        a = True
        while a == True:
            if num % 2 ==0 and num!=2 or num ==1 or num == 0: #checa se o numero eh par
                t+= 1
                num +=1
                
            else:
                while num > div: #checa todos os divisores impares ate ele mesmo
                    if num % div == 0:
                        div +=2
        a = False
        if a == False:
            lista[x] = num #retorna o numero primo
            x +=1
            t+=1
            num+=1
            div = 3
            
    return lista  