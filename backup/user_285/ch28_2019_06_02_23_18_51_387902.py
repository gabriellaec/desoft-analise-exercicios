v= float(input("Qual a velocidade do carro? "))
if v>80:
    multa= (v-80)*5
    print (format(multa, '.2f'))
else:
    print("não foi multado")
       