import sys.csv
for row in csv.reader('dados.csv'):
    print "\t".join(row)