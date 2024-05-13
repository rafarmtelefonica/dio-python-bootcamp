batata = 10
valor = [0]

def soma(valor, numero_um, numero_dois): # funcao com parametros nomeados (keyword) apenas
    print(f"Local {batata}")
    valor.append(numero_dois + numero_um)

def subtracao(numero_um, numero_dois, /): # funcao com parametros posicionais apenas
    return numero_dois - numero_um

soma(valor, 1, 2)
print(valor)
print(batata)
print(subtracao(1,3))