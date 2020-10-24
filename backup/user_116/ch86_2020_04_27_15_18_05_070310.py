with open("dados.csv","r") as arquivocsv:
    ler=arquivocsv.readlines()
    parastring="\t".join(ler)
    with open("dados.tsv","w") as arquivostsv:
        arquivostsv.write(parastring)
