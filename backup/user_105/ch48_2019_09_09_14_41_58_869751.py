x = input(' qual mes ')
meses = ['jan', 'fev', 'março', 'abril', 'maio', 'jun', 'jul', 'agost', 'setembro', 'out', 'novem', 'dezembro']
i = 0
while i < 12:
    if x == meses[i]:
        print (i+1)
    i += 1