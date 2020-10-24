senha="desisto"
tentativa=input("Escreva a senha ")
num_tentativas=1
limite_tentativas=3

while num_tentativas < limite_tentativas:
       num_tentativas+=1
       tentativa=input("Escreva a senha ")
       if tentativa==senha:
              print("Acertou!!")
              break
else:
       print("Errou")
              