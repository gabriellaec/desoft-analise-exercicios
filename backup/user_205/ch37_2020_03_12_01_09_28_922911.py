n = 0 
while (n<10):
    senha = "desisto"
    n +=1
    palavra = input("Digite a palavra: ")
    if palavra != senha:
        print ("Tente novamente")
    else: 
        print ("Você acertou a senha!")
        break
    