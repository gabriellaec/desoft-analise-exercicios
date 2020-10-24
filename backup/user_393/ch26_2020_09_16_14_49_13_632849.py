v= float(input("Valor da casa:"))
s= float(input("Salário:"))
t= float(input("Quantidade de meses a pagar:"))

if s < (v/t)*0.3:
    print("Empréstimo não aprovado")
    
else:
    print("Empréstimo aprovado")
    
         
