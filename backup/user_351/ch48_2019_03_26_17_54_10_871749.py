meses = ['jan','fev','mar','abril','maio','jun','jul','agst','set','out','nov','des']
mes = input("qual o mês?")
c = 0
while meses[c] != mes and c<12:
    c+=1
print (c + 1)