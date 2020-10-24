def calcula_tempo(dicionario):
    dic:{}	
	for k,v in dicionario.items():	        
    	dic[k]=(200/v)**0.5
    return dic