import sqlite3
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

banco = sqlite3.connect("gastos.db")
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, produto TEXT NOT NULL, valor REAL NOT NULL)")

# Função para obter texto do Entry (Input)

def getInput():

    if registro_produto.get().strip() == "" or registro_valor.get().strip() == "":
        return

    nomeProduto = str(registro_produto.get())

    try:
        valorProduto = float(registro_valor.get())
    except ValueError:
        print("O valor inserido é inválido")
        return

    cursor.execute("INSERT INTO gastos(produto, valor) VALUES(?, ?)", (nomeProduto.capitalize(), valorProduto))
    banco.commit()

    registro_produto.delete(0, customtkinter.END)
    registro_valor.delete(0, customtkinter.END)
    registro_produto.focus_set()

    print(f"Produto salvo")

def mostrar_gastos():
    janela_gastos = customtkinter.CTkToplevel(window)
    janela_gastos.geometry("400x400")
    janela_gastos.title("Expenses")

    cursor.execute("SELECT produto, valor FROM gastos")
    resultados = cursor.fetchall()
    total = sum(valor for _, valor in resultados)

    texto_gastos = customtkinter.CTkTextbox(janela_gastos, width=350, height=300, font=("Arial", 22))
    texto_gastos.pack(padx=10, pady=10)

    texto_total = customtkinter.CTkLabel(janela_gastos, width=350, height=350, text=f"Total: R$ {total}", font=("Arial", 25))
    texto_total.pack(padx=10, pady=10)

    if resultados:
        for produto, valor in resultados:
            texto_gastos.insert("end", f"{produto} - R$ {valor:.2f}\n")
    else:
        texto_gastos.insert("end", "Nenhum Gasto cadastrado")

    texto_gastos.configure(state="disabled")

#Janela Tkinter

window = customtkinter.CTk()

window.geometry("400x500")
window.resizable(width = False, height= False)
window.title("SaveFin")

idiomaVar = customtkinter.StringVar()
idiomaVar.set("English")

frame = customtkinter.CTkFrame(window, bg_color="black")
frame.pack(expand=True)

registro_produto = customtkinter.CTkEntry(frame, width=250, placeholder_text="Product", font=("Arial", 25))
registro_produto.pack(padx=35, pady=35)

registro_valor = customtkinter.CTkEntry(frame, width=250, placeholder_text="Price", font=("Arial", 25))
registro_valor.pack(padx=35, pady=35)

botao_submit = customtkinter.CTkButton(frame, width=125, height=35, text="Submit", command=getInput, font=("Arial", 25))
botao_submit.pack(padx=35, pady=35)

botao_gastos = customtkinter.CTkButton(window, width=125, height=35, text="Expenses", command=mostrar_gastos, font=("Arial", 25))
botao_gastos.pack(padx=35, pady=35)

window.mainloop()
