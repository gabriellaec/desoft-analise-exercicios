def total_do_semestre_por_bairro(d1):

    contador = 0
    soma = 0
    fatura = dict()
    for k,v in d1.items():
        soma = 0
        for i in v:
            soma += i
            contador += 1
            if contador == 6:
                contador = 0
            
                break
        fatura[k] = soma
        
    return(fatura)