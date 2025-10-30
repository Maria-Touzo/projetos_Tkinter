import ttkbootstrap as ttk

def adicionar_vinho():
    adicionar = [nome_vinho.get(), local.get(), tipo_vinho.get(), ano_colheita.get(), qtde_stock.get()]

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

ttk.Button(janela, text="ADICIONAR",  padding=10, width=16, command="").pack(pady=10)

#criando a janela do treeview
treeview = ttk.Treeview(janela)
treeview.pack(pady=15)

#cria as colounas, ma não mostra elas na tela
treeview["columns"] = ("nome_vinho", "pais", "tipo", "ano_colheita", "qtde_stock")
#se eu não quiser a coluna que vem por padrão
treeview["show"] = "headings"

#para mostrar os nomes na tela
#0 já vem por padrão, INUTIL
# treeview.heading("#0", text="coluna chata")
treeview.heading("nome_vinho", text="nome completo")
treeview.heading("pais", text="País/Região")
treeview.heading("tipo", text="Tipos do vinho")
treeview.heading("ano_colheita", text="Ano da colheita")
treeview.heading("qtde_stock", text="Quantidade stock")

ttk.Button(janela, text="DELETAR", padding=10, width=16, command="").pack(pady=10)

ttk.Button(janela, text="AVALIAR", padding=10, width=16, command="").pack()
janela.mainloop() 

