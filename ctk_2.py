import customtkinter as ctk

# criando a janela
janela = ctk.CTk()

# título da janela
janela.title("Nome do Programa")

# geometria (dimensões da janela)
janela.geometry("1000x700")
janela.maxsize(width=1000, height=700)
janela.minsize(width=800, height=500)
# impedir o redimensionamento da janela, ou permitir apenas da largura ou da altura.
janela.resizable(width=False, height=False)

# função para fechar a janela (usar com alguma condicional)
#janela.iconify()

#função para reabrir a janela
#janela.deiconify()





# executando o programa
janela.mainloop()