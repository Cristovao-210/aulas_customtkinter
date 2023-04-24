import customtkinter as ctk

# criando a janela
janela = ctk.CTk()

# configurando o tema da janela
janela._set_appearance_mode("dark")

# exemplo de botaão
btn = ctk.CTkButton(janela, text="Botão de Salvar", bg_color="red", text_color="red", corner_radius=80)
btn.pack()

# executando o programa
janela.mainloop()