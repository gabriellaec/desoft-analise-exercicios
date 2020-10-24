lista=["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
m=input("qual o mes? ")
i=0
e_o_mes=False
while e_o_mes==False:
    if m==lista[i]:
        e_o_mes=True
    else:
        i+=1
print(i+1)
