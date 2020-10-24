def eh_primo(n):
    if n<0:
        resultado="numero negativo"
    for i in range(2, n):
	    if n % i  == 0:
		    resultado="nao eh primo"
		    break
    else:
	    resultado="eh primo"
    return resultado
print(eh_primo(n)) 
def maior_primo_menor_que(n):
    if n<0:
        final=-1
    elif eh_primo(n)=="eh primo":
        final=n
    else:
        j=0
        while eh_primo(n-j)=="nao eh primo":
            eh_primo(n-j)
            j+=1
        final=n-j
    return final