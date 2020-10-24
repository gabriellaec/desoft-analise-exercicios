def primeiras_ocorrencias(string):
    caract_ocorr = {}
    for e in string:
        if e not in caract_ocorr:
            caract_ocorr[e] = string.find(e)
            
	return caract_ocorr   