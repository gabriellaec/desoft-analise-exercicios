with open("dados.csv", "r") as file:
    with open("dados.tsv", "w") as file2:
        file2.write(file.read().replace(",", "\t")