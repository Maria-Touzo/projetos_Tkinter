import ttkbootstrap as ttk

class Lista_de_tarefas:

    def __init__(self):
        #criando a janela
        self.janela = ttk.Window(themename= "minty")
        #título janela
        self.janela.title("Lista de tarefas")
        #maximiza a janela
        self.janela.wm_state("zoomed")
        #não alterar tamanho 
        self.janela.resizable(False, False)
        #adicionando texto
        label_título = ttk.Label(self.janela, text="Minha lista de tarefas!",
                                 foreground="black",
                                 font=("Times New Roman", 32))
        label_título.pack()
        #criando a caixa de texto 
        self.entry_adicionar = ttk.Entry()
        self.entry_adicionar.pack(pady=20)
    
    def run(self):
        self.janela.mainloop()
    
if __name__ == "__main__":
    janela = Lista_de_tarefas()
    janela.run()