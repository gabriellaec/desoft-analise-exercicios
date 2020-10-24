def login_disponivel(a, l1):
    contador = ''
    conta = 0
    lista = l1
    if l1 == []:
            return a
        
    for i in l1:
         
        '''if a not in l1:
            return a'''
        
        if a in l1:
            if i == a+str(contador) or i == a+str(conta):
                conta += 1
            
        
        
        else: 
            return a
        

            
    return a + str(conta)

lista = list()   
while True:
    a = input("Digite um usuario: ")
    
    if a == 'fim':
        break
    
    x = login_disponivel(a, lista)
    
    lista.append(x)
    
for i in lista:
    print(i)