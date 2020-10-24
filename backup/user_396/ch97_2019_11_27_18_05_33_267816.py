def total_do_semestre_por_bairro(x):
    for e in x:
    	valor = x[e]
    	i = 0
    	soma = 0
    	while i < len(valor):
        	soma += valor[i]
        	i+=1
        	novo_dic = {}
        	novo_dic[e] = soma

