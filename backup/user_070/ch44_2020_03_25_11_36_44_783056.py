ano = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
n = int(input('qual mes? '))
i = 1
while n>=i:
    resp = ano[n-1]
    i += 1
print(resp)