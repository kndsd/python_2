import customtkinter as ctk 
ctk.set_appearance_mode("dark")

janela = ctk.CTk()
janela.geometry("500x500")
janela.title('sistema de Acesso - 2026')
janela.iconbitmap('')

titulo = ctk.CTkLabel(janela,
text=("sistema de login"),
text_color=('#6cf56e'),
font=("arial",40))

login = ctk.CTkEntry(janela,
placeholder_text="Digite seu login",
width=300,
height=40,
border_width=2,
corner_radius=10)

senha = ctk.CTkEntry(janela,
placeholder_text="Digite sua senha",
width=300,
height=40,
border_width=2,
corner_radius=10,
show="*")

butao = ctk.CTkButton(janela,
text="Entrar",
width=300,
height=40,
border_width=2,
corner_radius=10,
command=lambda: print("login:", login.get(), "senha:", senha.get()),
cursor = "hand2")





titulo.pack()
login.pack(pady=10)
senha.pack(pady=10)
butao.pack(pady=10)
janela.mainloop()