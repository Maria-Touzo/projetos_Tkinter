import ttkbootstrap as  tk

class janela_principal: 
    """Classe para a criação da janela principal"""

    def __init__(self):
        #Criando uma janela 
        self.janela = tk.Window(themename= "minty")

        #Criando o título
        self.janela.title("hello world")

        #mudando a cor da janela

                                                                                                                                                                                                                        
        #colocando ícone 
        self.janela.iconbitmap("02_Hello_World_com_classes/watermelon.ico")

        #aletrando o tamanho
        #800 e 400 é altura e largura e os 200 é a posição
        self.janela.geometry("800x400+200+200")

        #janela maximizada
        self.janela.wm_state("zoomed")

        #impedindo que o usuário redimensione a janela
        self.janela.resizable(False, False)

        #inserindo um texto
        self.label_titulo = tk.Label(self.janela, text= "Helloo world!", 
                            
                                foreground= "black", #cor da fonte
                                font=("Arial", 24)) #fonte

        #desenha os componentes na janela "titulo do projeto"
        self.label_titulo.pack(pady=30) #pady adiciona um espaço vertical

        #interagindo com o usuário, mostra o texto "digite o seu nome"
        self.label_nome = tk.Label(self.janela, text="Digite o seu nome: ",
                
                            foreground= "black",
                            font= ("Arial", 14))

        #desenhando os componenetes 
        self.label_nome.pack(pady=10) #pady é pra não ficar grudado

        #caixa de texto para a pessoa digitar o nome
        self.entry_nome = tk.Entry(self.janela)
        self.entry_nome.pack()


        #botão para o programa desejar "bom dia"
        botao_bom_dia = tk.Button(self.janela, text= "enviar", command= self.desejar_bom_dia)
        botao_bom_dia.pack(pady= 10)

        #desejando o bom dia
        self.label_resultado = tk.Label(self.janela, text= "",
                                font=("Arial, 30"),
                                foreground="black")
        self.label_resultado.pack(pady=10)

    def run(self):
        """inicia a janela"""
        #loop para manter a janela aberta
        self.janela.mainloop()

    #função do botão
    def desejar_bom_dia(self):
        """Esta função pega o nome digitado na caixa de texto e deseja um bom dia"""
        nome = self.entry_nome.get()
        self.label_resultado.configure(text= f"bom dia, {nome}")
