import ttkbootstrap as ttk

frutas_sorteio = ["🍈",]

class Janela:
    def __init__(self):
        #Criando a janela
        self.janela = ttk.Window(themename= "darkly")

        #criando o título
        self.janela.title("Sorteio de frutas")

        #deixando a janela maximizada
        self.janela.wm_state("zoomed")

        #para o usuário não redimensionar a janela
        self.janela.resizable(False, False)

        ttk.Label(self.janela, text="Sorteio de frutas", 
                  anchor= "w",
                  font=("Arial", 50)).pack()

    def run(self):
        """Iniciar a janela"""
        self.janela.mainloop()

if __name__ == "__main__":
    janela_principal = Janela()
    janela_principal.run()
