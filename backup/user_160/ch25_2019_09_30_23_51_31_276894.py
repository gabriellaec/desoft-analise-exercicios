a = input("Qual a distância que o usuário pretende percorrer?")
def preco(a):
    if a <= 200:
        y = 0.50*a
        print y
    else:
        y = 100 + 0.45*(a-200)
        print y