distância=int(input("Qual é a distância em km: "))
if distância<=200:
    print ("O preço é: R$ {0.2f}".format(distância*0.5))
else:
    print ("O preço é: R$ {0.2f}".format((200*0.5) + (distância-200)*0.45)) 

