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
                        bg = "white", 
                        foreground= "black",
                        font=("Arial", 24))

#desenha os componentes na janela "titulo do projeto"
label_titulo.pack(pady=30) #pady adiciona um espaço vertical

#interagindo com o usuário, mostra o texto "digite o seu nome"
label_nome = tk.Label(janela, text="Digite o seu nome: ",
                      bg = "white",
                      foreground= "black",
                      font= ("Arial", 14))
#desenhando os componenetes 
label_nome.pack(pady=10)

#caixa de texto para a pessoa digitar o nome
entry_nome = tk.Entry(janela)
entry_nome.pack()

#botão para o programa desejar "bom dia"
botao_bom_dia = tk.Button(janela, text= "enviar")
botao_bom_dia.pack(pady= 10)

#desejando o bom dia
label_resultado = tk.Label(janela, text= "bom dia")
label_resultado.pack(pady=10)

#loop para manter a janela aberta
janela.mainloop()