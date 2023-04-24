import customtkinter as ctk

# criando a janela
janela = ctk.CTk()

# título da janela
janela.title("Nome do Programa")

janela.geometry("1000x700")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=300)
janela.resizable(width=False, height=False)

janela._set_appearance_mode("dark") # pega o tema do sistema

# Frame
frame_1 = ctk.CTkFrame(master=janela, width=200, height=330, bg_color="teal", fg_color="teal").place(x=10, y=60)
frame_2 = ctk.CTkFrame(janela, width=200, height=330, bg_color="teal", border_color="white",border_width=5, fg_color="teal", corner_radius=20).place(x=230, y=60)
frame_3 = ctk.CTkFrame(janela, width=200, height=330, bg_color="teal", fg_color="teal").place(x=450, y=60)
frame_4 = ctk.CTkFrame(janela, width=200, height=330, bg_color="teal", fg_color="teal").place(x=670, y=60)



# executando o programa
janela.mainloop()