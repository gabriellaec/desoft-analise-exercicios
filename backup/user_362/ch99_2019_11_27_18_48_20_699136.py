def login_disponivel(login_usuario,lista_nomes):
    contador=1
    for i in lista_nomes:
        if login_usuario==lista_nomes[i]:
            login_novo_usuario=login_usuario[contador]
        contador+=1
    return login_novo_usuario
  
    