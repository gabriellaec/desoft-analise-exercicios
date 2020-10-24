def aniversariantes_de_setembro(dictio):
    aniv_set=dict()
    for i in dictio():
    	x=i.values().replace("/","[]")
		z=x.split("[]")
        if z[1]="09":
        	aniv_set[i.keys()]=i.values()
    return aniv_set
        