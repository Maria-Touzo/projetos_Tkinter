import tkinter as  tk

#Criando uma janela 
janela = tk.Tk()

#Criando o título
janela.title("hello world")

#mudando a cor da janela
janela.configure(bg="#FACADA")

#colocando ícone 
janela.iconbitmap("watermelon.ico")

#aletrando o tamanho
#800 e 400 é altura e largura e os 200 é a posição
janela.geometry("800x400+200+200")

#janela maximizada
janela.wm_state("zoomed")

#impedindo que o usuário redimensione a janela
janela.resizable(False, False)

#inserindo um texto
label_titulo = tk.Label(janela, text= "Helloo world!", 
                        bg = "white", #cor de fundo
                        foreground= "black", #cor da fonte
                        font=("Arial", 24)) #fonte

#desenha os componentes na janela "titulo do projeto"
label_titulo.pack(pady=30) #pady adiciona um espaço vertical

#interagindo com o usuário, mostra o texto "digite o seu nome"
label_nome = tk.Label(janela, text="Digite o seu nome: ",
                      bg = "white",
                      foreground= "black",
                      font= ("Arial", 14))

#desenhando os componenetes 
label_nome.pack(pady=10) #pady é pra não ficar grudado

#caixa de texto para a pessoa digitar o nome
entry_nome = tk.Entry(janela)
entry_nome.pack()

#função do botão
def desejar_bom_dia():
    """Esta função pega o nome digitado na caixa de texto e deseja um bom dia"""
    nome = entry_nome.get()
    label_resultado.configure(text= f"bom dia, {nome}")

#botão para o programa desejar "bom dia"
botao_bom_dia = tk.Button(janela, text= "enviar", command= desejar_bom_dia)
botao_bom_dia.pack(pady= 10)

#desejando o bom dia
label_resultado = tk.Label(janela, text= "",
                           font=("Arial, 30"),
                           foreground="black")
label_resultado.pack(pady=10)

#loop para manter a janela aberta
janela.mainloop()