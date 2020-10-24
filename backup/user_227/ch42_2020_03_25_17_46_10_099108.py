lista=[]

resposta = input("Digite palavra: ")
print(resposta)

while resposta != "fim":
    
    primeira_letra = resposta[0]
    if primeira_letra == 'a':
       lista.append(resposta)
       
    resposta = input("Digite palavra: ")
    print(resposta)