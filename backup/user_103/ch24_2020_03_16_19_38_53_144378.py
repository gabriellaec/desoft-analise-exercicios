def calcula_aumento(b):
    b=input("Qual é o seu salário:")
    if int(b)>1250:
            return 1.1*b
    if int(b)<=1250:
            return 1.15*b
            
          