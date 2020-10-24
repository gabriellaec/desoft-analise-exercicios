x=input("")
lista=["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
i=0
m=0
while i<len(lista):
    if lista[i]==x:
        m=i+1
    i+=1
    
return m
             