import customtkinter as ctk

ctk.set_appearance_mode("dark")


def calcular_imposto():
    try:
        # Obtém e converte o valor do rendimento mensal
        rendimento = float(entry_rendimento.get())
        
        # Lógica simplificada de alíquotas do IRRF (Base aproximada)
        if rendimento <= 2259.20:
            imposto = 0.0
            aliquota = "Isento"
            cor_aliquota = "#2ECC71"  # Verde
        elif rendimento <= 2826.65:
            imposto = (rendimento * 0.075) - 169.44
            aliquota = "7.5%"
            cor_aliquota = "#FFA500"  # Laranja
        elif rendimento <= 3751.05:
            imposto = (rendimento * 0.15) - 381.44
            aliquota = "15.0%"
            cor_aliquota = "#FFA500"  # Laranja
        elif rendimento <= 4664.68:
            imposto = (rendimento * 0.225) - 662.77
            aliquota = "22.5%"
            cor_aliquota = "#FF4D4D"  # Vermelho
        else:
            imposto = (rendimento * 0.275) - 896.00
            aliquota = "27.5%"
            cor_aliquota = "#FF4D4D"  # Vermelho
            
        # Garante que o imposto não fique negativo
        if imposto < 0:
            imposto = 0.0
            
        # Atualiza os textos na interface
        lbl_imposto_valor.configure(text=f"R$ {imposto:.2f}")
        lbl_situacao_valor.configure(text=aliquota, text_color=cor_aliquota)
        
    except ValueError:
        # Caso o usuário digite algo inválido ou deixe vazio
        lbl_imposto_valor.configure(text="Erro")
        lbl_situacao_valor.configure(text="Preencha o campo!", text_color="#FF4D4D")


# Configuração da Janela
janela = ctk.CTk()
janela.geometry("400x480")
janela.resizable(False, False)
janela.title("Calculadora de Imposto de Renda")

# Nome do Contribuinte
lbl_nome = ctk.CTkLabel(janela, text="Nome do Contribuinte:", font=("Arial", 14))
lbl_nome.pack(anchor="w", padx=30, pady=(20, 2))

entry_nome = ctk.CTkEntry(janela, width=340, height=40, placeholder_text="Digite seu nome")
entry_nome.pack(padx=30, pady=2)

# Rendimento Mensal
lbl_rendimento = ctk.CTkLabel(janela, text="Rendimento Mensal (R$):", font=("Arial", 14))
lbl_rendimento.pack(anchor="w", padx=30, pady=(10, 2))

entry_rendimento = ctk.CTkEntry(janela, width=340, height=40, placeholder_text="Ex: 3000.00")
entry_rendimento.pack(padx=30, pady=2)

# Botão Calcular
b_calcular = ctk.CTkButton(
    janela,
    width=340,
    height=45,
    text="CALCULAR IMPOSTO",
    font=("Arial", 14),
    fg_color="#A51F1F",
    command=calcular_imposto
)
b_calcular.pack(pady=25)

# Frame de Resultado
frame_resultado = ctk.CTkFrame(janela, width=340, height=130, corner_radius=10)
frame_resultado.pack(padx=30, pady=5, fill="x")

lbl_imposto_texto = ctk.CTkLabel(frame_resultado, text="Imposto Devido:", font=("Arial", 16))
lbl_imposto_texto.place(x=20, y=25)

lbl_imposto_valor = ctk.CTkLabel(frame_resultado, text="R$ -", font=("Arial", 20, "bold"))
lbl_imposto_valor.place(x=160, y=23)

lbl_situacao_texto = ctk.CTkLabel(frame_resultado, text="Alíquota:", font=("Arial", 16))
lbl_situacao_texto.place(x=20, y=75)

lbl_situacao_valor = ctk.CTkLabel(frame_resultado, text="-", font=("Arial", 18, "bold"))
lbl_situacao_valor.place(x=160, y=75)

janela.mainloop()
