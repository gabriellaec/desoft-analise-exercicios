def preco(d):
    if d<=200:
        return "O preço da passagem é {0:.2f}".format(0.5*d)
    else:
        return "O preço da passagem é {0:.2f}".format(0.5*200+(d-200)*0.45)

x=float(input("Quantos km? "))
print(preco(x))