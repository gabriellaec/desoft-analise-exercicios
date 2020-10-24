idade= int(input("informe a sua idade: "))
if idade<18 :
    print ("Não está liberado")
elif idade>18 and idade<21:
    print ("Liberado BRASIL")
elif idade>21:
    print ("Liberado EUA e BRASIL")