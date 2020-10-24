i=0
invalid=True 
soma=0
while invalid:
    if i<=99:
        soma+=1*(1/2)**i
        i+=1
    else:
        invalid=False
print(soma)
#==========================
soma=0.0
for val in range (99):
    soma=soma+1*(1/2)**val
print (soma)


