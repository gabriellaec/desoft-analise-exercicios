a = 0
y = True
lista_final = [0]
h = 0
while y: 
    
    if a == 998:
            y = False
    
    
    def collatz(a):
        w = int(a)
        lista = [0]
        lista[0] = w
        p = a
        y = True
        n = 0
        
        while lista[n] != 1:
            

            if ( lista[n] % 2 == 0):
                b = lista[n]/2 
                lista.append(round(b,0))
                n = n + 1

            
            else:
                b = (3*lista[n])+1
                lista.append(round(b,0))
                n = n + 1

        h = len(lista)
        lista_final.append(h)
        #print(lista_final)
        #return(lista)
        
        
        
    a = a + 1 
    
    print(collatz(a))
    #print(lista_final)
    t = max(lista_final)+1
print(t)