def reducao_expc_vida (cigarros, anos):
    reducao = (cigarros/144) * 365
    return reducao

num_cigarros = int(input("Entre com o numero de cigarros consumidos por dia:"))
num_anos = int(input("Entre com o número de anos de tabagismo:"))
queda_expc_de_vida = reducao_expc_vida(num_cigarros, num_anos)
print("Sua expectativa de vida foi reduzida em {0:.1f} dias." .format(queda_expc_de_vida))