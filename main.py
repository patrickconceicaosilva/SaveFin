import customtkinter
import json

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

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

    registro_produto.delete(0, customtkinter.END)
    registro_valor.delete(0, customtkinter.END)
    registro_produto.focus_set()

    print(f"Produto salvo em {arquivo_JSON}")

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
