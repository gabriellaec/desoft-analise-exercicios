import csv
with open ('dados.csv','r') as csvin, open ('dados.tsv', 'w') as tsvout:
    csvin=csv.reader(csvin)
    tsvout=csv.write(tsvout, delimiter=' ')
    for row in csvin:
        tsvout.writerow(row)