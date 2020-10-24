			return False
		elif x % t !=0:
			t += 1
			return True
def imprime_primos(x):
	var = 1
	cnt = 1
	while cnt <= x:
		if eh_primo(var):
			print(var)
			cnt = cnt + 1
			var = var + 1
		else:
			var = var + 1
n = int(input('Digite um numero: '))
imprime_primos(n)