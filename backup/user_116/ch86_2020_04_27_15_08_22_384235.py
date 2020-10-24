with open("dados.csv","r") as arquivocsv:
    ler=arquivocsv.read()
    paratsv="\t".join(ler)
    with open("dados.tsv","w") as arquivostsv:
        arquivostsv.write(paratsv)
        