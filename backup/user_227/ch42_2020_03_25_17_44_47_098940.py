lista=[]

resposta = input("Digite palavra: ")

while resposta != "fim":
    
    primeira_letra = resposta[0]
    if primeira_letra == 'a':
       lista.append(resposta)
if resposta == 'fim':
    lista.append(resposta)
       
    resposta = input("Digite palavra: ")