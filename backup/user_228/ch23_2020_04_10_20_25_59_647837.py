a=int(input("Qual a velocidade?"))
if a > 80:
    b=(a-80)*5
    print("Você foi multado em {:.2f} reais".format(b))
else:
    print('Não foi multado')
          
      