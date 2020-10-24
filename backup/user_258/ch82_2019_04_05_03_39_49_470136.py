def primeiras_ocorrencias(string):
    dic={}
    for e in string:
        for i in range(len(string)):
        	if e not in dic:
            	dic[e]=i
    return dic
      
            