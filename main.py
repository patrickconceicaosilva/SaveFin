import sqlite3
import customtkinter
import json

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

    cursor.execute("INSERT INTO gastos(produto, valor) VALUES(?, ?)", (nomeProduto, valorProduto))
    banco.commit()

    registro_produto.delete(0, customtkinter.END)
    registro_valor.delete(0, customtkinter.END)
    registro_produto.focus_set()

    print(f"Produto salvo")

#Temporarily disabled

# def mudarIdioma():
#     idioma = idiomaVar.get()

#     if idioma == "Português":
#         botao_submit.configure(text="Enviar")
#     elif idioma == "English":
#         botao_submit.configure(text="Submit")
    
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

#Temporarily disabled

#Language Selector

# dropDownIdioma = customtkinter.CTkOptionMenu(
#     window,
#     variable=idiomaVar,
#     values=["English", "Português"],
#     command=lambda:mudarIdioma(),
#     font=("Arial", 15)
# )
# dropDownIdioma.pack(padx=35, pady=25)

window.mainloop()
