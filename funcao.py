def print_livro(nome_livro, nome_autor):
    print(f"Nome do livro: {nome_livro}")
    print(f"Nome do autor: {nome_autor}")


livro = "1984"
autor = "George Orwel"
print_livro(livro, autor)


def calcular_imc(altura, peso):
    imc = (peso)/(altura**2)
    return imc


print("IMC: %.2f" % calcular_imc(1.81, 78))
