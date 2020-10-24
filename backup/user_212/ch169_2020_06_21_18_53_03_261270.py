def login_disponivel (string, lista_uso):
    nome = string
    
    if nome not in lista_uso:
        return string 
    
    else: 
        i = 1
        while string in lista_uso:
            string = nome + str(i)
            i +=1
            
        return string
            
usuario = str(input("Digite um usuário"))
lista_nomes_disponiveis =[]

while usuario != 'fim':
    disponivel = login_disponivel (usuario, lista_nomes_disponiveis)
    lista_nomes_disponiveis.append(disponivel)
    usuario = str(input("Digite um usuário"))
    
    
for n in lista_nomes_disponiveis:
    print(n)
    