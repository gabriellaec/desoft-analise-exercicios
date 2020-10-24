def primo(x):
	i = 2
	while i<x:
		if x%i==0:
			return False
		i+=1
	return True

def primos_entre(a,b):
	l=[]
	for i in range(a,b):
		if primo(i):
			l.append(i)
	return l

print(primos_entre(1, 100))