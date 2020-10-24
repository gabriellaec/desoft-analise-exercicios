def Munchhausen (numero): #Criar uma função para verificar munchhausen
    if numero < 1: #Desconsiderando numeros que 1
        return False
    
    else:  #Verificar se é munchhausen
        nString = str(numero) #Transformando o numero em string
        listaElevados = [] #Lista
        soma = 0 #Soma dos valores da lista

        for n in nString: #Percorrendo os digitos do numero
            elevado = int(n) ** int(n) #Transformando string em numero e elevando pelo seu valor
            listaElevados.append(elevado) #Adicionando o resultado na lista de elevados
    
        i = 0
        while i < len(listaElevados): #percorrendo a lista dos digitos elevados
            soma += listaElevados[i] #somando o elevado com o valor anterior de soma
            i += 1 #incrementando 1 ao indicie
            
        return soma == numero #Retorna em Booleano se é ou não um número de Munchhausen