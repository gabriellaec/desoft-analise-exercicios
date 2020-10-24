with open('dados.csv', 'r') as arq:
    cont = arq.read()
word = cont.split(',')
word_tsv = "\t".join(word)
with open('dados.tsv' , 'w') as arq_tsv:
    cont_tsv = arq_tsv.write(word_tsv)
