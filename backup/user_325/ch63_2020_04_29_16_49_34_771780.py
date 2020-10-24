def nome_usuario(email):
    i = 0
    a = email.find('@')
    return (email[0:a])
print(nome_usuario("alex@gmail.com"))
    