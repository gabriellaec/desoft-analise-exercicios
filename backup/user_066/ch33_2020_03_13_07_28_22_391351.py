def primos_entre(a, b):
    def eh_primo(j): #Função que testa se é primo: True se primo - False se não primo
        x = 3
        a = 1 
        z = True
        if j == 1 or j == 0: 
            #print('O número {0} não é primo'.format(j))
            z = False
        elif j == 2 or j == 3:
            z = True
            #print('O número {0} é primo'.format(j))
        else:
            if j%2 == 0:
                #print('O número {0} não é primo'.format(j))
                z = False
            else:
                while x<j and a!=0: 
                    k = j%x
                    x += 2  
                    if k == 0:
                        a = 0
                        z = False
                        #print('O número {0} não é primo'.format(j))
                    if a != 0:   
                        #print('O número {0} é primo'.format(j))
                        a = 0    
        return z
    p = 0
    j = a
    while j<=b:
        if eh_primo(j) == True:
            p += 1
            j += 1
        else:
            j += 1
	return p