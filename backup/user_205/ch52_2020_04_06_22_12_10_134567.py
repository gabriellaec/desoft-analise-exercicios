def calcula_total_da_nota(lista1,lista2):
    soma=0
    for produto in range(len(lista1)):
        for quantidade in range(len(lista2)):
            soma = soma + lista1[produto]*lista2[quantidade]
    return (soma)
   