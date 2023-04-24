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

# Tabview (Abas)
tab_view = ctk.CTkTabview(master=janela, width=600, corner_radius=20, bg_color="lightgray", border_width=5, 
                          border_color="red", segmented_button_fg_color="yellow",
                          segmented_button_selected_color="green",
                          segmented_button_selected_hover_color="brown",
                          segmented_button_unselected_color="purple",
                          segmented_button_unselected_hover_color="brown",
                          text_color="black")
tab_view.pack()
lista_tabs = ["SERVIDOR", "ÓRGÃO", "ENTIDADE", "DADOS BANCÁRIOS", "ATIVIDADES"]
for ind, tab in enumerate(lista_tabs):
    tab_view.add(tab)
    tab_view.tab(tab).grid_columnconfigure(ind, weight=1)

# adicionando conteúdo as tabs
dados_servidor = {"NOME": "Márcio Cristóvão", "CPF": "04611332616","CARGO": "Assistente em Administração"}
for dado in dados_servidor:
    texto = ctk.CTkLabel(tab_view.tab("SERVIDOR"), text=f'{dado}: {dados_servidor[dado]}')
    texto.pack()

dados_orgao = {"NOME": "Universidade de Brasília", "CNPJ": "123456980001/00"}
for dado in dados_orgao:
    texto = ctk.CTkLabel(tab_view.tab("ÓRGÃO"), text=f'{dado}: {dados_orgao[dado]}')
    texto.pack()




# executando o programa
janela.mainloop()