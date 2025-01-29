import json

arquivo_JSON = "Gastos.json"

try:
    with open (arquivo_JSON, "r") as arquivo:
        gastos = json.load(arquivo)
except FileNotFoundError:
    print("O arquivo JSON não existe\nExecute primeiro o main.py")
    gastos = []

total = 0

for produto in gastos:
    total += float(produto["valor"])
    
print(f"O total gasto foi R${total:,.2f}")