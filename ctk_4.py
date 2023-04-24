import customtkinter as ctk

# criando a janela
janela = ctk.CTk()

# título da janela
janela.title("Nome do Programa")

# configurando o tema da janela
#janela._set_appearance_mode("dark")
#janela._set_appearance_mode("ligth")
janela._set_appearance_mode("system") # pega o tema do sistema

# geometria (dimensões da janela)
janela.geometry("1000x700")
janela.maxsize(width=1000, height=700)
janela.minsize(width=800, height=500)
# impedir o redimensionamento da janela, ou permitir apenas da largura ou da altura.
janela.resizable(width=False, height=False)

# criando uma nova janela
def nova_tela():
    nova_janela = ctk.CTkToplevel(janela, fg_color="teal")
    nova_janela.geometry("400x300")
    #janela.iconify()

btn_nova_tela = ctk.CTkButton(master=janela, text="Abrir nova janela", command=nova_tela).place(x=300, y=200)



# executando o programa
janela.mainloop()