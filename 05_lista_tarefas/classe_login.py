import ttkbootstrap as ttk
import tkinter.messagebox


class Login:

    def __init__(self, janela_pai):

        #estou transformando o parametro e atributo para poder 
        # usar em qualquer método (função)
        self.janela_pai = janela_pai

        #criando a janela
        self.janela = ttk.Toplevel(janela_pai)

        #título janela
        self.janela.title("Lista de tarefas ")

        #maximizando a janela
        self.janela.wm_state("zoomed")

        #não alterar tamanho
        self.janela.resizable(False, False)

        #configurando para que quando feche a janela de login ele encerre o programa
        self.janela.protocol("WM_DELETE_WINDOW",  self.sair)

        #escrevendo "login"
        label_login= ttk.Label(self.janela, text= "Login:",
                                        foreground="black",
                                        font=("Times New Roman",32 ))
        label_login.pack(pady=10)

        label_usuario= ttk.Label(self.janela, text= "Usuário:",
                                        foreground="black",
                                        font=("Times New Roman",12 ))
        label_usuario.pack(pady=10)


        #criando a caixa de texto usuário
        self.entry_usuario = ttk.Entry(self.janela)
        self.entry_usuario.pack(pady=10)

        #escrevendo "senha"
        label_senha = ttk.Label(self.janela, text= "Senha:",
                                        foreground="black",
                                        font=("Times New Roman",12 ))
        label_senha.pack(pady=10)

        #criando a caixa de texto senha
        self.entry_senha = ttk.Entry(master=self.janela, show="***")
        self.entry_senha.pack(pady=10)

        #criando um frame
        self.frame_botao = ttk.Frame(self.janela)
        self.frame_botao.pack()

        #criando o botão login
        self.botao_login = ttk.Button(self.frame_botao, text= "Logar", padding=10, width=10, command= self.logar )
        self.botao_login.pack(side="left", padx=10)

        #criando o botão sair
        sair = ttk.Button( self.frame_botao, text= "Sair", padding=10, width=10, command=self.sair  )
        sair.pack(side="right")
       
    def run(self):
        """Iniciar a janela"""
        self.janela.mainloop()

    def logar(self):
        #pegando os valores das caixas de entrada
        senha_usuario = self.entry_senha.get()
        login_usuario = self.entry_usuario.get()

        #verificando o login e a senha
        if login_usuario == "Godofredo" and senha_usuario == "amogirassol":
            #tkinter.messagebox.showinfo(title="Login realizado com sucesso", message="parabéns!")
            self.janela.destroy()
            #reexibe a janela principal, janela de tarefas 
            self.janela_pai.deiconify()
            self.janela_pai.wm_state("zoomed")
        else:
            tkinter.messagebox.showerror(title="ERRO", message="login ou senha incorreta")
        
    
    def sair(self):
        pergunta = tkinter.messagebox.askyesno(title="Sair", message="Tem certeza que deseja sair?")
        if pergunta == True:
            exit()
        else: 
            False
    
    

if __name__ == "__main__":
    janela = Login()
    janela.run()