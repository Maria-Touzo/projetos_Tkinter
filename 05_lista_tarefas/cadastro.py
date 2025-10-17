import ttkbootstrap as ttk

class Janela_cadastro:

    def __init__(self, janela_pai):

        #Criando a janela filha
        self.janela_cadastro = ttk.Toplevel(janela_pai)

        self.janela_cadastro.wm_state("zoomed")

        #criando o título
        ttk.Label(self.janela_cadastro,
                  text= "Cadastro de usuário").pack(padx=10)
        
        #label do nome
        ttk.Label(self.janela_cadastro,
                  text= "Digite o seu nome completo: ").pack(pady=10)
        
        #Criando a caixa de texto do nome
        caixa_nome = ttk.Entry(self.janela_cadastro)
        caixa_nome.pack()

        #Label da senha
        ttk.Label(self.janela_cadastro,
                  text= "Digite a sua senha: ").pack(pady=10)
        
        #caixa de texto senha
        caixa_senha = ttk.Entry(self.janela_cadastro)
        caixa_senha.pack()

    def run (self):
        self.janela_cadastro.mainloop()

if __name__ == "__main__":
    Janela_cadastro = Janela_cadastro(ttk.Window(themename="minty"))
    Janela_cadastro.run()