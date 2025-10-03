import ttkbootstrap as ttk
from tkinter import Listbox, END
from tkinter import messagebox
import sqlite3


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

        #criando um frame
        frame_add = ttk.Frame(self.janela)
        frame_add.pack(fill= "x", padx=10)
        #criando a caixa de texto 
        self.add_tarefa = ttk.Entry(frame_add)
        self.add_tarefa.pack(side="left",pady=20, expand=True, fill= "x")

        #criando o botão login
        self.botao_add = ttk.Button(frame_add, text= "Adicionar", command=self.adicionar_tarefa)
        self.botao_add.pack(side="right",padx= 10)

        self.lista = Listbox(self.janela, font=("Times New Roman",12), height=10)
        self.lista.pack(pady=20, padx=20, fill='both', expand = True)

        frame_botao = ttk.Frame(self.janela)
        frame_botao.pack(side="bottom", padx=20, pady=20)

        botao_excluir = ttk.Button(frame_botao, text= "Excluir", width=50, style="danger", command=self.excluir_item)
        botao_excluir.pack(side="left", padx=10)

        botao_concluir = ttk.Button(frame_botao, text= "Marcar como concluído", width=50, style="sucess", command=self.tarefa_concluida)
        botao_concluir.pack(side="right", padx=10)

        #fazendo conexão com o banco de dados
        conexao = sqlite3.connect("05_lista_tarefas/bd_lista_tarefa.sqlite")
        #criando o cursor (quem fica responsável pelo banco de dados)
        cursor = conexao.cursor()
        #criando uma tabela pro banco de dados
        sql_para_criar_tabela = """
                          CREATE TABLE tarefas (
                          codigo integer primary key autoincrement, 
                          tarefa varchar(200)
                          );      
                          """
        #executando o banco de dados
        cursor.execute(sql_para_criar_tabela)
        #comitando a tebela
        conexao.commit()
        #fechando a conexão (não precisa necessariamente fechar o cursor, só fechando a conexão, automticamente já fecha o cursor)
        cursor.close()
        conexao.close()

    def adicionar_tarefa(self):
        #pegando o texto da caixa de textp
        tarefa = self.add_tarefa.get()

        #inserindo a tarfa na lista
        self.lista.insert('end', tarefa)

    def excluir_item (self):
         excluir_indice = self.lista.curselection()

         if excluir_indice:
            self.lista.delete(excluir_indice)
         else:
            messagebox.showerror(title="Erro", message="Por favor, selecione um ítem para excluir!")

    def tarefa_concluida(self):
        marcar_tarefa_concluida = self.lista.curselection()

        if marcar_tarefa_concluida:
            texto_lista = self.lista.get(marcar_tarefa_concluida)
            self.lista.delete(marcar_tarefa_concluida)
            self.lista.insert(marcar_tarefa_concluida, texto_lista + "[Concluido]")
        else:
             messagebox.showerror(title="Erro", message="Por favor, selecione um ítem para marcar!")

    
    def run(self):
        self.janela.mainloop()

    
if __name__ == "__main__":
    janela = Lista_de_tarefas()
    janela.run()