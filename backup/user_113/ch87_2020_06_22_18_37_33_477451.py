import csv
with open (churras.txt):
    i = 1
    while i < len(churras.txt):
        custo = churras.txt[i][2] + churras.txt[i-1][2]
        i += 1