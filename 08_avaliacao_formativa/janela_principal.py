import ttkbootstrap as ttk

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

    def run(self):
        """Iniciar a janela"""
        self.janela.mainloop()
if __name__ == "__main__":
    janela_principal = Janela()
    janela_principal.run()
