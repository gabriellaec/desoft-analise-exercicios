def calcula_valor_devido(x,y,z):
    emprestado = x
    meses = y
    juros = z
 calcula_valor_devido = x*((1+z)**y)
x = 10
y = 2
z = 0.1
print(calcula_valor_devido(10,2,0.1))
 