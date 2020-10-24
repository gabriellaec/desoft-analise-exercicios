def simplifica_dict(d):
	d1={}
	for i,j in d.items():
    	if j not in d1.values():
        	d1[i]=j
print(d1)