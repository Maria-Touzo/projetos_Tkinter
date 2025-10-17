import ttkbootstrap as ttk
import sqlite3

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
        self.caixa_nome = ttk.Entry(self.janela_cadastro)
        self.caixa_nome.pack()

        #Label do usuario
        ttk.Label(self.janela_cadastro,
                  text= "Digite o seu usuario: ").pack(pady=10)
        
        #caixa de texto usuario
        self.usuario_cadastro = ttk.Entry(self.janela_cadastro)
        self.usuario_cadastro.pack()

        #Label da senha
        ttk.Label(self.janela_cadastro,
                  text= "Digite a sua senha: ").pack(pady=10)
        
        #caixa de texto senha
        self.caixa_senha = ttk.Entry(self.janela_cadastro)
        self.caixa_senha.pack()

        ttk.Button(self.janela_cadastro, 
                   text="Cadastrar",
                   command= self.inserir_usuario).pack(pady=15)

    def criar_tabela_usuario (self):

        #conectando ao banco de dados
        conexao = sqlite3.connect("./bd_lista_tarefa.sqlite")

        #criar cursor
        conexao = conexao.cursor()

        #executar o comando
        cursor = cursor.execute("""CREATE TABLE IF NOT EXISTS usuario(
                                nome VARCHAR(80),
                                usuario VARCHAR(20),
                                senha VARCHAR(20);
                                                """)
        
        #comito a transação
        conexao.commit()

        #fechando a conexao
        conexao.close
                    
    def inserir_usuario (self):

        #criar conexão
        conexao = sqlite3.connect("./bd_lista_tarefa.sqlite")

        #criar cursor
        cursor = conexao.cursor()

        nome = self.caixa_nome.get()
        usuario = self.usuario_cadastro.get()
        senha = self.caixa_senha.get()

        #executar
        cursor.execute("""INSERT INTO usuario
                            (nome,
                            usuario,
                            senha)
                        VALUES 
                                (?
                                ?,
                                ?);""",
                       (nome,
                        usuario,
                        senha)
                       )
        
        #salvando a transação
        conexao.commit()

        #fechando
        conexao.close()
            
    def run (self):
        self.janela_cadastro.mainloop()

if __name__ == "__main__":
    Janela_cadastro = Janela_cadastro(ttk.Window(themename="minty"))
    Janela_cadastro.run()