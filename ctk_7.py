import customtkinter as ctk

# criando a janela
janela = ctk.CTk()

# título da janela
janela.title("Nome do Programa")

janela.geometry("900x550")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=300)
janela.resizable(width=False, height=False)
janela._set_appearance_mode("dark") # pega o tema do sistema

# Textbox (caixas de texto)
caixa_texto = ctk.CTkTextbox(janela, width=200, height=350, scrollbar_button_color="red", activate_scrollbars=True, 
                             border_width=3, border_color="pink",scrollbar_button_hover_color="yellow",
                             corner_radius=15, fg_color="teal", border_spacing=20)
caixa_texto.pack()

# inserir texto
caixa_texto.insert("0.0", "Testando colocar texto na caixa de texto."*20)


# executando o programa
janela.mainloop()