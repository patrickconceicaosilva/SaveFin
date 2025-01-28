import json

registro_produto = input("Produto: ")
registro_valor = float(input("Valor: "))

produtos = {}
produtos["produto"] = registro_produto
produtos["valor"] = registro_valor

arquivo_JSON = "Gastos.json"


try:
    with open(arquivo_JSON, "r") as arquivo:
        gastos = json.load(arquivo)
except FileNotFoundError:
    gastos = []
except json.JSONDecodeError:
    print("O arquivo JSON contém dados inválidos")
    gastos = []


gastos.append(produtos)

with open(arquivo_JSON, "w") as arquivo:
    json.dump(gastos, arquivo, indent=4)

print(f"Produto salvo em {arquivo_JSON}")