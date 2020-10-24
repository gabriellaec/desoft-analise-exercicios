def lista_primos (num):
    lista = []*num
	if num == 1:
		return 2
    lista.append(2)
	i=2
	while i < num:
		if num % i == 0:
			lista.append(num)
		i = i+1
