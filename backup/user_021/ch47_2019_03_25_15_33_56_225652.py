meses=["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
mes=input("Numero do mes? ")
i=0
while i<len(meses):
    if mes==meses[i]:
        print(meses[i])
    i+=1