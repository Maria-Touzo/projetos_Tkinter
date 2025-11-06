import ttkbootstrap as ttk
import sqlite3
import tkinter
from tkinter import messagebox


def adicionar_vinho():
    adicionar = [nome_vinho.get(), local.get(), tipo_vinho.get(), ano_colheita.get(), qtde_stock.get()]

    conexao = sqlite3.connect("07_projeto_vinho/bd_projeto_vinho.sqlite")
    cursor = conexao.cursor()
    sql_insert = """
                    INSERT INTO vinho (nome_vinho, regiao_pais, tipo, ano_colheita, qtde_stock)
                    VALUES (?, ?, ?, ?, ?);
                    """
    cursor.execute(sql_insert,adicionar)
    conexao.commit()
    conexao.close()
    atualizar_treeview()

def deletar_vinho():
 #selecionando o ítem para remoção
    item_selecionado = treeview.selection()
    if item_selecionado:
        #pegando os valores da linha
        valores_selecionados = treeview.item(item_selecionado, "values")
        #atribuindo o id = 0
        id_vinho = valores_selecionados[0]
        #deletando
        treeview.delete(item_selecionado)
        # Conecta ao banco e deleta o registro
        conexao = sqlite3.connect("07_projeto_vinho/bd_projeto_vinho.sqlite")
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM vinho WHERE id = ?", [id_vinho])
        conexao.commit()
        conexao.close()
    else:
        messagebox.showerror(title="Erro", message="Por favor, selecione um ítem para excluir!")


def atualizar_treeview():

    for linha in treeview.get_children():
        treeview.delete(linha)
    
    conexao = sqlite3.connect("07_projeto_vinho/bd_projeto_vinho.sqlite")
    cursor = conexao.cursor()
    sql_select = """SELECT id, nome_vinho, regiao_pais, tipo, ano_colheita, qtde_stock FROM vinho;"""
    cursor.execute(sql_select)
    resultado = cursor.fetchall()
    conexao.commit()
    conexao.close()

    for linha in resultado:
        treeview.insert("","end",values =linha)

def avaliacao():

    item_selecionado = treeview.selection()
    if not item_selecionado:
        messagebox.showerror("ERRO!", "Para avaliar, você tem que selecionar um ítem")
        return
    janela_2 = ttk.Toplevel(janela)
    janela_2.title("Avaliação")
    janela_2.wm_state("zoomed")
    janela.resizable(False,False)

    ttk.Label(janela_2, text="Avalie o vinho com valores de 0 a 100", font=("Helvetica", 14,"bold")).pack(pady=10)
   
    ttk.Label(janela_2, text="Aroma",
               anchor= "w",
            font=50).pack(fill= "x", padx=20, pady=10)
    
    aroma = ttk.Entry(janela_2)
    aroma.pack( fill= "x", padx=10)

    ttk.Label(janela_2, text="Sabor",
               anchor= "w",
            font=50).pack(fill= "x", padx=20, pady=10)
    
    sabor = ttk.Entry(janela_2)
    sabor.pack( fill= "x", padx=10)


    ttk.Button(janela_2, text="Salvar avaliação", bootstyle="success", command=salvar_avaliacao).pack(pady=10)

    conexao = sqlite3.connect("07_projeto_vinho/bd_projeto_vinho.sqlite")
    cursor = conexao.cursor()
    tabela = """
        CREATE TABLE IF NOT EXISTS avaliacao (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aroma FLOAT,
        sabor FLOAT
               );
""" 
    cursor.execute(tabela)
    conexao.commit()
    conexao.close()

def salvar_avaliacao():
    avaliacao  = [aroma.get(), sabor.get()]

    conexao = sqlite3.connect("07_projeto_vinho/bd_projeto_vinho.sqlite")
    cursor = conexao.cursor()
    sql_insert = """
                    INSERT INTO avaliacao ( aroma , sabor )
                    VALUES (?, ?, ?, ?, ?);
                    """
    cursor.execute(sql_insert,avaliacao)
    conexao.commit()
    conexao.close()



janela = ttk.Window(themename="minty")

janela.title("Degustação de vinhos")
            
janela.wm_state("zoomed")

janela.resizable(False, False)

ttk.Label(janela, text="Nome do vinho",
          font=50).pack(fill= "x", padx=20, pady=10)

nome_vinho = ttk.Entry(janela)
nome_vinho.pack( fill= "x", padx=10, pady=10)

ttk.Label(janela, text="País/Região:",
          anchor= "w",
          font=50).pack(fill= "x", padx=20, pady=10)

local = ttk.Entry(janela)
local.pack(  fill= "x", padx=10)

ttk.Label(janela, text="Tipo do vinho",
          anchor= "w",
          font=50).pack(fill= "x", padx=20, pady=10)

tipo_vinho = ttk.Entry(janela)
tipo_vinho.pack(pady=10,  fill= "x", padx=10)

ttk.Label(janela, text="Ano da colheita:",
          anchor= "w",
          font=50).pack(fill= "x", padx=20, pady=10)

ano_colheita= ttk.Entry(janela)
ano_colheita.pack(pady=10, fill= "x", padx=10)

ttk.Label(janela, text="Quantidade stock:",
          anchor= "w",
          font=50).pack(fill= "x", padx=20, pady=10)

qtde_stock= ttk.Entry(janela)
qtde_stock.pack(pady=10, fill= "x", padx=10)

ttk.Button(janela, text="ADICIONAR",  padding=10, width=16, command=adicionar_vinho).pack(pady=10)

#criando a janela do treeview
treeview = ttk.Treeview(janela)
treeview.pack(pady=15)

#cria as colounas, ma não mostra elas na tela
treeview["columns"] = ("id","nome_vinho", "pais", "tipo", "ano_colheita", "qtde_stock")
#se eu não quiser a coluna que vem por padrão
treeview["show"] = "headings"

#para mostrar os nomes na tela
#0 já vem por padrão, INUTIL
# treeview.heading("#0", text="coluna chata")
treeview.heading("id", text="id")
treeview.heading("nome_vinho", text="nome completo")
treeview.heading("pais", text="País/Região")
treeview.heading("tipo", text="Tipos do vinho")
treeview.heading("ano_colheita", text="Ano da colheita")
treeview.heading("qtde_stock", text="Quantidade stock")



ttk.Button(janela, text="DELETAR", padding=10, width=16, command=deletar_vinho).pack(pady=10)

ttk.Button(janela, text="AVALIAR", padding=10, width=16, command=avaliacao).pack()


conexao = sqlite3.connect("07_projeto_vinho/bd_projeto_vinho.sqlite")
cursor = conexao.cursor()
criar_tabela = """
        CREATE TABLE IF NOT EXISTS vinho (
               id   INTEGER PRIMARY KEY AUTOINCREMENT,
               nome_vinho VARCHAR(20),
               regiao_pais VARCHAR(20),
               tipo VARCHAR (20),
               ano_colheita INT,
               qtde_stock INT
               );
"""
cursor.execute(criar_tabela)
conexao.commit()
conexao.close()

atualizar_treeview()
janela.mainloop() 