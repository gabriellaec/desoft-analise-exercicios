

with open('dados.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('dados.tsv','w') as new_file:
        csv_writer = csv.writer(new_file, delimiter = '	')

            for line in csv_reader:
                csv_writer.writerow(line)