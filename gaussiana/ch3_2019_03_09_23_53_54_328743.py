def calcula_gaussiana(x,μ,σ):
  
	f = (1/σ*(2* math.pi)**1/2)** (- o.5((x - μ)/ σ)**2)
	return f
print(calcula_gaussiana(10,10,10))
