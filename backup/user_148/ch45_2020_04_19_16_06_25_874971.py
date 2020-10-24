núm = []
n = int(input('Digite um número: '))

while n > 0:
    n = int(input('Digite um número: '))
    núm.append(n)

núm.sort(reverse=True)
print(núm)
