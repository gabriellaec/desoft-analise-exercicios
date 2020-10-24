def login_disponivel(x):
    nome = input("Qual é o seu nome? ")
    i = 0
    if nome not in x:
        x.append(nome)
    else:
        i += 1
        novo_nome = nome + str(i)
        print("nome indisponivel")
        print("use o nome: ", novo_nome)
        
    return x

print(simplifica_dict(['andre', 'fabio', 'lucio', 'lucio1']))