mes=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
n=[1,2,3,4,5,6,7,8,9,10,11,12]
a=input('Qual mes?')
i=0
while i<len(n):
    if a==mes[i]:
        print(n[i])
    i+=1

