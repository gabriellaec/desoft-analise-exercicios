d=int(input('distância?'))
if d <= 200:
    a = 0.5 * d
else:
    a = 0.45 * d + 100
print ('{0:.2f}'.format(a))