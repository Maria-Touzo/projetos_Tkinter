import tkinter as tk 
from class_robo import Boot_gemini

#sempre que essa classe for chamda, a janela principal será aberta 
class janela_principal():

    def __init__(self): # o init roda uma única vez
        #Criando uma janela
        self.janela = tk.Tk()
        #criando o título
        self.janela.title("Dr. Casa")
        #mudando a cor da janela
        self.janela.configure(bg = "pink")
        #janela maximizada
        self.janela.wm_state("zoomed")
        #para o usuário não redimensionar a janela
        self.janela.resizable(False,False)
        #inserindo o título
        self.label_titulo = tk.Label(self.janela, text= "Seja bem-vindo ao chat!",
                                    foreground= "black",
                                    font= ("Arial", 24))
        #desenhando os componenets da janela
        self.label_titulo.pack( pady = 30)
        #inserindo texto
        self.label_pergunta = tk.Label(self.janela, text= "Olá, sou a DRA. Casa, e estou aqui para lhe ajudar, qual a sua dúvida de hoje?",
                                    foreground= "black",
                                    font= ("Arial", 16))
        #desenhando os componenets da janela
        self.label_pergunta.pack( pady = 30)
        #caixa de texto para o usuário digitar
        self.entry_usuario = tk.Entry(self.janela,)
        self.entry_usuario.pack()
        #botão par o usuário enviar a pergunta
        self.botao_enviar = tk.Button(self.janela, text= "PERGUNTAR")
        self.botao_enviar.pack(pady = 30)

        #respondendo
        self.label_resposta = tk.Label(self.janela, text= "RESPOSTA",
                                font=("Arial, 14"),
                                foreground="black")
        self.label_resposta.pack(pady=10)

        #criando o objeto robo (instancindo a classe)
        self.robo = Boot_gemini ()

    def run (self):
        self.janela.mainloop()

    def responder (self):
        pergunta = self.entry_usuario.get() #pegou o texto que eu digitei
        resposta = self.robo.responder(pergunta) #mandar a pergunta pro robô
        self.label_resposta.config(text= resposta)
        


if __name__ == "__main__":
   chat = janela_principal()
   chat.run()
   
   
