deposito_inicial = float(input("qual o depósito inicial?"))
taxa_de_juros = (float(input("qual a taxa de juros, meu queridx?"))/100) +1

valores_mensais=[0]*24
valores_mensais[0]=deposito_inicial

i=1
while i<24:
    valores_mensais[i]=valores_mensais[i-1]*taxa_de_juros
    i+=1

for e in valores_mensais:
    print("{0:.2f}".format(e))
print("{0:.2f}".format(valores_mensais[23]-valores_mensais[0]))
