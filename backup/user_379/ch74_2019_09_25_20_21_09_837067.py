def conta_bigramas(string):
	contador={}
    i=0
    while i<len(string)-1:
        key = string[i]+string[i+1]
        if key in contador:
			contador[key] += 1
        else:
            contador[key] = 1
        i+=1
	       