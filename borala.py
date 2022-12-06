print("RESTAURANTE DO BORALA")

print(f"Tabela de desconto: \n Se o cliente comprar mais que 3 pratos principais 4% \n Se o valor total da nota for maior que 500,00 6% \n Se tiver cupom de desconto válido 10% BORALA10 \n Se tiver cupom de desconto válido 5% BORALA05 \n Se for a primeira vez que visita o restaurante 5%")

qtdPessoas = int(input("Digite a quantidade de pessoas: "))
racharConta = input("O cliente deseja rachar a conta?: ")

# Desconto nota
valorTotal = float(input("Digite o valor total da nota fiscal: "))
if valorTotal >= 500:
    descNota = valorTotal - (6/100)
    if racharConta == "S":
        print("----------------------------------------------")
        print(f"Valor total da nota fiscal: {valorTotal}")
        print(f"Valor total da nota com desconto: {descNota}")
        print(f"Número de pessoas: {qtdPessoas}")
        print(f"Total por pessoa {descNota / qtdPessoas}")
        print("----------------------------------------------")
    else:
        print("----------------------------------------------")
        print(f"Valor total da nota fiscal: {valorTotal}")
        print(f"Valor total da nota com desconto: {descNota}")
        print(f"Número de pessoas: {qtdPessoas}")
        print("----------------------------------------------")
elif valorTotal >= 1:
    if racharConta == "S":
        print("----------------------------------------------")
        print(f"Valor total da nota fiscal: {valorTotal}")
        print(f"Valor total da nota com desconto: 0")
        print(f"Número de pessoas: {qtdPessoas}")
        print(f"Total por pessoa: {valorTotal / qtdPessoas}")
        print("----------------------------------------------")
    else:
        print("----------------------------------------------")
        print(f"Valor total da nota fiscal: {valorTotal}")
        print(f"Valor total da nota com desconto: 0")
        print(f"Número de pessoas: {qtdPessoas}")
        print("----------------------------------------------")
else:
    print("Valor inválido. Digite novamente")
    valorTotal = float(input("Digite o valor total da nota fiscal: "))
    if valorTotal >= 500:
        descNota = valorTotal - (6/100)
        if racharConta == "S":
            print("----------------------------------------------")
            print(f"Valor total da nota fiscal: {valorTotal}")
            print(f"Valor total da nota com desconto: {descNota}")
            print(f"Número de pessoas: {qtdPessoas}")
            print(f"Total por pessoa {descNota / qtdPessoas}")
            print("----------------------------------------------")
        elif racharConta == "N":
            print("----------------------------------------------")
            print(f"Valor total da nota fiscal: {valorTotal}")
            print(f"Valor total da nota com desconto: {descNota}")
            print(f"Número de pessoas: {qtdPessoas}")
            print("----------------------------------------------")
    elif valorTotal >= 1:
        if racharConta == "S":
            print("----------------------------------------------")
            print(f"Valor total da nota fiscal: {valorTotal}")
            print(f"Valor total da nota com desconto: 0")
            print(f"Número de pessoas: {qtdPessoas}")
            print(f"Total por pessoa: {valorTotal / qtdPessoas}")
            print("----------------------------------------------")
        elif racharConta == "N":
            print("----------------------------------------------")
            print(f"Valor total da nota fiscal: {valorTotal}")
            print(f"Valor total da nota com desconto: 0")
            print(f"Número de pessoas: {qtdPessoas}")
            print("----------------------------------------------")

# Desconto pratos
qntdPrato = int(input("Qual a quantidade de pratos principais pedidos?: "))
if qntdPrato >= 3:
    descPrato = valorTotal - (4/100)
    if racharConta == "S":
        print("----------------------------------------------")
        print(f"Valor total da nota fiscal: {valorTotal}")
        print(f"Valor total da nota com desconto: {descPrato}")
        print(f"Número de pessoas: {qtdPessoas}")
        print(f"Total por pessoa {descPrato / qtdPessoas}")
        print("----------------------------------------------")
    elif racharConta == "N":
        print("----------------------------------------------")
        print(f"Valor total da nota fiscal: {valorTotal}")
        print(f"Valor total da nota com desconto: {descPrato}")
        print(f"Número de pessoas: {qtdPessoas}")
        print("----------------------------------------------")
elif qntdPrato >= 1:
    if racharConta == "S":
        print("----------------------------------------------")
        print(f"Valor total da nota fiscal: {valorTotal}")
        print(f"Valor total da nota com desconto: 0")
        print(f"Número de pessoas: {qtdPessoas}")
        print(f"Total por pessoa: {valorTotal / qtdPessoas}")
        print("----------------------------------------------")
    elif racharConta == "N":
        print("----------------------------------------------")
        print(f"Valor total da nota fiscal: {valorTotal}")
        print(f"Valor total da nota com desconto: 0")
        print(f"Número de pessoas: {qtdPessoas}")
        print("----------------------------------------------")
else:
    print("Número de pratos principais inválido. Digite novamente")
    qntdPrato = int(input("Qual a quantidade de pratos principais pedidos?: "))
    if qntdPrato >= 3:
        descPrato = valorTotal - (4/100)
        if racharConta == "S":
            print("----------------------------------------------")
            print(f"Valor total da nota fiscal: {valorTotal}")
            print(f"Valor total da nota com desconto: {descPrato}")
            print(f"Número de pessoas: {qtdPessoas}")
            print(f"Total por pessoa {descPrato / qtdPessoas}")
            print("----------------------------------------------")
        elif racharConta == "N":
            print("----------------------------------------------")
            print(f"Valor total da nota fiscal: {valorTotal}")
            print(f"Valor total da nota com desconto: {descPrato}")
            print(f"Número de pessoas: {qtdPessoas}")
            print("----------------------------------------------")
    elif qntdPrato >= 1:
        if racharConta == "S":
            print("----------------------------------------------")
            print(f"Valor total da nota fiscal: {valorTotal}")
            print(f"Valor total da nota com desconto: 0")
            print(f"Número de pessoas: {qtdPessoas}")
            print(f"Total por pessoa: {valorTotal / qtdPessoas}")
            print("----------------------------------------------")
        elif racharConta == "N":
            print("----------------------------------------------")
            print(f"Valor total da nota fiscal: {valorTotal}")
            print(f"Valor total da nota com desconto: 0")
            print(f"Número de pessoas: {qtdPessoas}")
            print("----------------------------------------------")

