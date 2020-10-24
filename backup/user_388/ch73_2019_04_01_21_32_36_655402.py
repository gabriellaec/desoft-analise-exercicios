def remove_vogais(x):
    l=[]
    for i in x:
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
        	l.append(i)
    p = ''
    for i in l:
    	p+=i
    return p


