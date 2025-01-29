import tkinter
import json

# Função para obter texto do Entry (Input)

def getInput():

    if registro_produto.get().strip() == "" or registro_valor.get().strip() == "":
        return

    nomeProduto = registro_produto.get()
    valorProduto = registro_valor.get()

    produtos = {}
    produtos["produto"] = nomeProduto
    produtos["valor"] = valorProduto

    arquivo_JSON = "Gastos.json"
    
    try:
        with open(arquivo_JSON, "r") as arquivo:
            gastos = json.load(arquivo)
    except FileNotFoundError:
        gastos = []
    except json.JSONDecodeError:
        gastos = []

    gastos.append(produtos)

    with open(arquivo_JSON, "w") as arquivo:
        json.dump(gastos, arquivo, indent=4)

    registro_produto.delete(0, tkinter.END)
    registro_valor.delete(0, tkinter.END)
    registro_produto.focus_set()

    print(f"Produto salvo em {arquivo_JSON}")
    
#Janela Tkinter

window = tkinter.Tk()

window.geometry("400x500")
window.resizable(width = False, height= False)
window.title("SaveFin")

frame = tkinter.Frame(window)
frame.pack(expand=True)

label_produto = tkinter.Label(frame, text="Produto", font=("Arial", 15))
label_produto.pack(pady=20)
registro_produto = tkinter.Entry(frame, font=("Arial", 15))
registro_produto.pack()

label_valor = tkinter.Label(frame, text="Valor", font=("Arial", 15))
label_valor.pack(pady=20)
registro_valor = tkinter.Entry(frame, font=("Arial", 15))
registro_valor.pack()

botao_registro = tkinter.Button(frame, text="Registrar", command=getInput, font=("Arial", 15))
botao_registro.pack(pady=20)

window.mainloop()
