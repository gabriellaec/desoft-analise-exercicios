n = int(input('Insira o número referencia '))
def maior_primo_menor_que(n):
    def eh_primo(n):
        x = 3
        a = 1 
        z = True
        if n == 1 or n == 0: 
            #print('O número {0} não é primo'.format(n))
            z = False
        elif n == 2 or n == 3:
            #print('O número {0} é primo'.format(n))
            z = True
        else:
            if n%2 == 0:#testa se o número é par
                #print('O número {0} não é primo'.format(n))
                z = False
            else:
                while x<n and a!=0: 
                    k = n%x
                    x += 2  
                    if k == 0:
                        a = 0
                        z = False
                        #print('O número {0} não é primo'.format(n))
                if a != 0:   
                    #print('O número {0} é primo'.format(n))
                    a = 0    
        return z
    if n < 0:
        print('-1')
        return -1
    else:
        while eh_primo(n) != True:
            if n<0:
                print('Não ha números primos menores que este ')
                return -1
            else:
                n = n - 1
        print(n)
        return n