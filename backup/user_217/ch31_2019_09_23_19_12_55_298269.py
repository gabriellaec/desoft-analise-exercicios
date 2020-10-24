a=int(input("Qual valor da casa?: "))
b = int(input('Qual é o salario?: '))
c= int(input("Qual é a quantidade de anos?: "))    
    
vp = a/c
        
if vp >= (0.3*b):
    print('Empréstimo não aprovado')
    
else: 
    print('Empréstimo aprovado')