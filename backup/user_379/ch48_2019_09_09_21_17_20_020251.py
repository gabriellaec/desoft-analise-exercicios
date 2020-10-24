mes=["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
x=input("digite o mês")
i=0
while mes[i]<len(mes):
    if mes[i]==x:
        print(i+1)
    i+=1
