soma=0.0
termos=[1]*100
for i,e in enumerate(termos):
    termos[i]=1/(2**i)
    soma += termos[i]
print(soma)