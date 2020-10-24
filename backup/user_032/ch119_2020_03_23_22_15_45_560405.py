razao = x/(n-1)
if x>0 and n>0:
    def calcula_euler(razao,n):
        ex = (1*((razao**n)-1))/(razao-1)
        return ex	
    print(calcula_euler(razao,n))