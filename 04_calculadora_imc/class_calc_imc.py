import ttkbootstrap as ttk
import tkinter.messagebox

class Calculadora:
    """Classe para criar a calculadora"""

    def __init__(self):
        #Criando a janela
        self.janela = ttk.Window(themename= "minty")

        #criando o título
        self.janela.title("Calculadora IMC")

        #deixando a janela maximizada
        self.janela.wm_state("zoomed")

        #para o usuário não redimensionar a janela
        self.janela.resizable(False, False)

        #inserindo o título
        self.label_título = ttk.Label(self.janela, text="Calculadora IMC",
                                      foreground= "black",
                                      font=("Arial", 14))
        
        #desenhando os componentres da tela
        self.label_título.pack(pady= 30)

        #inserindo o subtítulo
        self.label_subtitulo = ttk.Label(self.janela, text="Aqui você poderá calcular o IMC colocando o seu peso e a sua altura nos campos abaixo:",
                                         foreground= "black",
                                         font=("Arial", 12))

        #desenhando o subtítulo
        self.label_subtitulo.pack(pady=30)

        #pedindo o peso da pessoa
        self.label_peso = ttk.Label(self.janela, text= "digite o seu peso (KG) aqui:",
                                    foreground= "black",
                                    font=("Arial", 12))
        
        #desenhando a pergunta
        self.label_peso.pack(pady=10)

        #caixa de texto do peso
        self.entry_peso = ttk.Entry(self.janela)
        self.entry_peso.pack()

        #pedindo a altura da pessoa
        self.label_altura = ttk.Label(self.janela, text= "digite a sua altura (m)² aqui:",
                                      foreground= "black",
                                      font=("Arial", 12))
        
        #desnhando a outra pergunta
        self.label_altura.pack(pady= 10 )

        #caixa de texto altura
        self.entry_altura = ttk.Entry(self.janela)
        self.entry_altura.pack()

        #botão para a resposta
        self.botao_resposta = ttk.Button(self.janela, text= "enviar", command= self.botao_responder)
        self.botao_resposta.pack(pady= 10)

        #colocando o resultado
        self.label_resultado = ttk.Label(self.janela, text="", 
                                          foreground="black",
                                          font= ("Arial", 12))
                                        
        self.label_resultado.pack(pady=10)

        #colocando a classificação
        self.label_classifi = ttk.Label(self.janela, text="",
                                             foreground= "black",
                                             font=("Arial",12))
        self.label_classifi.pack(pady=10)

    def run(self):
        """Iniciar a janela"""
        self.janela.mainloop()

    def botao_responder(self):
        #pegando o peso e a altura que o usuário colocou
        self.pergunta_peso = self.entry_peso.get()
        self.perguntar_altura = self.entry_altura.get()

        try: 
            #convertendo para float
            self.peso = float(self.entry_peso.get())
            self.altura = float(self.entry_altura.get())
            #calculei o peso
            self.calculando = self.peso / (self.altura * self.altura)
        except: 
            tkinter.messagebox.showerror(title="ERRO", message="Valores incorretos")

        #arredondando o resultado
        self.calculando = round(self.calculando,2)
        #resposta
        self.label_resultado.configure(text= f"seu imc é {self.calculando}")

        #classificação
        if self.calculando < 18.5:
            classificacao = "baixo peso"

        elif self.calculando >= 18.5 and self.calculando <=24.9:
            classificacao = "normoponderal"

        elif self.calculando >= 25 and self.calculando <=29.9:
            classificacao = "pré-obesidade"
        
        elif self.calculando >= 30 and self.calculando <=34.9:
            classificacao = "obesidade grau I"
        
        elif self.calculando >= 35 and self.calculando <= 39.9:
            classificacao = "obesidade grau II"

        elif self.calculando >= 40:
            classificacao = "obesidade mórbida" 

        self.label_classifi.configure(text= f"sua classificação é: {classificacao}")
        


if __name__ == "__main__":
    janela = Calculadora()
    janela.run()
