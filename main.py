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

def mudarIdioma():
    idioma = idiomaVar.get()

    if idioma == "Português":
        label_produto.config(text="Produto")
        label_valor.config(text="Valor")
        botao_submit.config(text="Enviar")
    else:
        label_produto.config(text="Product")
        label_valor.config(text="Price")
        botao_submit.config(text="Submit")
    
#Janela Tkinter

window = tkinter.Tk()

window.geometry("400x500")
window.resizable(width = False, height= False)
window.title("SaveFin")

idiomaVar = tkinter.StringVar()
idiomaVar.set("English")

frame = tkinter.Frame(window)
frame.pack(expand=True)

label_produto = tkinter.Label(frame, text="Product", font=("Arial", 15))
label_produto.pack(pady=20)
registro_produto = tkinter.Entry(frame, font=("Arial", 15))
registro_produto.pack()

label_valor = tkinter.Label(frame, text="Price", font=("Arial", 15))
label_valor.pack(pady=20)
registro_valor = tkinter.Entry(frame, font=("Arial", 15))
registro_valor.pack()

botao_submit = tkinter.Button(frame, text="Submit", command=getInput, font=("Arial", 15))
botao_submit.pack(pady=20)

dropDownIdioma = tkinter.OptionMenu(window, idiomaVar, "English", "Português", command=lambda _: mudarIdioma())
dropDownIdioma.pack()

window.mainloop()
