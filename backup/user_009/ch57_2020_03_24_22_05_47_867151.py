def verifica_progressao(l):
	if (l[0]+l[-1])*len(l)/2 == sum(l):
        return 'PA'
