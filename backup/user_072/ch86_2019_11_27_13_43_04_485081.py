import pandas as pd

# names of files to read from
readCSV = 'CSV_text.csv'
#readTSV = 'TSV_text.tsv'

# names of files to write to
writeTSV = 'TSV_text.tsv'
#writeCSV = 'CSV_text.csv'

# read the data
csv_read = pd.read_csv(readCSV)
#tsv_read = pd.read_csv(readTSV, sep='\t')

# print the first 10 records
#print(csv_read.head(10))
#print(tsv_read.head(5))

# write to files

with open(writeTSV,'w') as write_tsv:
    write_tsv.write(csv_read.to_csv(sep='\t', index=False))

#with open(writeCSV,'w') as write_csv:
#    write_csv.write(tsv_read.to_csv(sep=',', index=False))