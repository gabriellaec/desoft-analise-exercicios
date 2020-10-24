with open('dados.csv', 'r') as r_file:
    CSVdata = r_file.read()
    


with open('dados.tsv', 'w') as w_file:
    i=0
    while i <len(CSVdata):
        w_file.write(CSVdata[i] + '		')
        i+=2