def reducao_expc_vida (cigarros):
    reducao = cigarros*(1/144)
    return reducao

num_cigarros = int(input("Entre com o numero de cigarros:"))
queda_expc_de_vida = reducao_expc_vida(num_cigarros)
print("Sua expectativa de vida foi reduzida em {0} dias." .format(queda_expc_de_vida))