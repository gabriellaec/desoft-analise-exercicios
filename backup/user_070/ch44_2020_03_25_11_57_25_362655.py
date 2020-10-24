ano = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
n = input('qual mes? ')
i = 0
resp = 1
while n!=ano[i]:
    i += 1
    resp += 1
print(resp)