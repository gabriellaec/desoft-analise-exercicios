lista=[]
palavra=input("Digite uma palara (digite fim para parar): ")
continua=True
while continua:
    if palavra!="fim" and palavra[0]=="a":
        lista.append(palavra)
        palavra=input("Digite uma palara (digite fim para parar): ")
    elif palavra!="fim" and palavra[0]!="a":
        palavra=input("Digite uma palara (digite fim para parar): ")
    else:
        print(lista)
        continua=False