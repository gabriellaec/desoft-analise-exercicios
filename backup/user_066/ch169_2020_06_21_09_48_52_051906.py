lista_users = []
dict_users = {}
def add_user(usuario):
    if usuario == 'fim':
        return dict_users
    if usuario in dict_users:
        dict_users[usuario] +=1
    else:
        dict_users[usuario] = 1
    return dict_users
user = input('insira o login ')
add_user(user)
while user!='fim':
    user = input('insira o login ')
    add_user(user)
for i,j in dict_users.items():
    k = 1
    lista_users.append(i) 
    while k<j:
        nome = i + str(k)
        lista_users.append(nome)
        k += 1
print(lista_users)