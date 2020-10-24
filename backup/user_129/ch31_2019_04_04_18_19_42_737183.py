x= int(input('quanto  custa a casa'))
y= int(input('qual seu salario'))
z= int(input('quantidade de anos a pagar'))
valor = x/z
z= z*12
if z > 0.3*y:
    print ('emprestimo aprovado')
else:
    print ('emprestimo nao aprovado')
       
             