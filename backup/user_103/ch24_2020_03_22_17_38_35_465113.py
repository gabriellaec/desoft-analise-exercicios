def calcula_aumento(b):
    b=float(input("Qual é o seu salário:"))   
    if b>1250:
        print ("O seu salário com aumento é: R$ {0:.2f}".format ((b*1.1)-b))
    elif b<=1250:
        print ("O seu salário com aumento é: R$ {0:.2f}".format ((b*1.15)-b))

            
          