import ttkbootstrap as ttk
import sqlite3
import random
from tkinter import messagebox

animais_sorteio = ["🐶", "🦊", "🐱‍🐉", "🐰", "🐬", "🐢"]

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
                  font=("helvetica", 24, "bold"), bootstyle="primary").pack(pady=10)
        
        frame_animais = ttk.Frame(self.janela)
        frame_animais.pack()

        # Criando o quadrado na onde ficará a primeira fruta
        self.animal_1 = ttk.Label(frame_animais,text="🐢", font= ("times new roman", 50), bootstyle="info", padding=10, relief="solid")
        self.animal_1.pack(side='left', padx=10, pady=30)

        # Criando o quadrado na onde ficará a segunda fruta
        self.animal_2 = ttk.Label(frame_animais,text="🐢", font= ("times new roman", 50), bootstyle="info", padding=10, relief="solid")
        self.animal_2.pack(side='left', padx=10, pady=30 )

        # Criando o quadrado na onde ficará a terceira fruta
        self.animal_3 = ttk.Label(frame_animais,text="🐢", font= ("times new roman", 50), bootstyle="info", padding=10, relief="solid")
        self.animal_3.pack(side='left', padx=10,  pady=30)

        #criando o botão sortear
        self.bt_sortear = ttk.Button(self.janela, text="SORTEAR!", 
                                     bootstyle="primary", 
                                     command="").pack()
        
        #começando a fazer a treeview

        #criando o título
        ttk.Label(self.janela, text="Jogadas", font=("helvetica", 14)).pack(pady=(10, 5))

        #a tabela ficará dentro desse frame
        treeview_frame = ttk.Frame(self.janela)
        treeview_frame.pack(fill="both", expand=True, padx=20, pady=10)

        #barra de rolagem
        scrollbar = ttk.Scrollbar(treeview_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        # tem apenas uma coluna
        cols = ('resultado',)
        self.treeview = ttk.Treeview(treeview_frame,
                                     columns= cols,
                                     show='headings',
                                     bootstyle="info",
                                     yscrollcommand=scrollbar.set)
        # Quando alguém mexer na barra de rolagem, faça o Treeview rolar para cima ou para baixo.
        scrollbar.config(command=self.treeview.yview)

        # Define o nome da coluna como “Resultado da Jogada”.
        self.treeview.heading('resultado', text='Resultado da Jogada')

        # configurando as colunas 
        self.treeview.column('resultado', width=450, anchor="center")
        self.treeview.pack(fill="both", expand=True)

        #criando a database do bcd
        self.criar_database()

        # atualizando a treeview
        self.atualizar_treeview()

    def criar_database(self):
        """
        Cria o banco e a tabela 'jogadas' (VERSÃO 3).
        A tabela terá APENAS 1 campo de dados (resultado).
        """
        conexao = sqlite3.connect("sorteio.db")
        cursor = conexao.cursor()
        
        # ATUALIZADO: Tabela com apenas id e resultado
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS jogadas (
                resultado TEXT NOT NULL
            )
        """)
        conexao.commit()
        conexao.close()

    def atualizar_treeview(self):
        """
        Busca (SELECT) todas as jogadas (VERSÃO 3).
        """
        conexao = sqlite3.connect("sorteio.db")
        cursor = conexao.cursor()
        
        # ATUALIZADO: SQL buscando apenas id e resultado
        sql = "SELECT resultado FROM jogadas"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        conexao.close()

        # Limpar o Treeview (para não duplicar)
        for i in self.treeview.get_children():
            self.treeview.delete(i)

        # Popular o Treeview
        for jogada in resultados:
            # A tupla 'jogada' já vem no formato (resultado),
            # exatamente o que o Treeview espera.
            self.treeview.insert("", "end", values=jogada)

    def run(self):
        """Iniciar a janela"""
        self.janela.mainloop()

if __name__ == "__main__":
    janela_principal = Janela()
    janela_principal.run()
