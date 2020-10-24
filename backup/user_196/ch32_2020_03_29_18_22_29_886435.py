def lista_primos (num):
    lista = []*num
	i=2
	if num == 1:
		return 2
    lista.append(2)
	while i < num:
		if num % i == 0:
			lista.append(num)
		i = i+1
