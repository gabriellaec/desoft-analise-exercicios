def resolve_equacao_1o_grau(a, b):
    raiz_da_equacao = -b/a
    print("A raiz da equacao é {0}".format(raiz_da_equacao))
a = float(input("Informe o coeficiente angular da reta: "))
b = float(input("Informe a constante da reta: "))
resolve_equacao_1o_grau(a, b)