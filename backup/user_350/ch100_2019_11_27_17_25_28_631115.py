a = True 
lista = []
lista_resp = []
while a :
    nome = input("digite nome")
    if nome == "fim":
        a = False
    else:
        lista.append(nome)
		lista_resp.append(login_disponivel(nome,lista))




        