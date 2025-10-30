import ttkbootstrap as ttk

def apagar_item():
    item_selecionado = treeview.selection()
    treeview.delete(item_selecionado)

#criando a janela
janela = ttk.Window(themename="minty")
janela.wm_state("zoomed")

#criando a janela do treeview
treeview = ttk.Treeview(janela)
treeview.pack(pady=15)

#cria as colounas, ma não mostra elas na tela
treeview["columns"] = ("nome", "idade", "cidade")
#se eu não quiser a coluna que vem por padrão
treeview["show"] = "headings"

#para mostrar os nomes na tela
#0 já vem por padrão, INUTIL
# treeview.heading("#0", text="coluna chata")
treeview.heading("nome", text="nome completo")
treeview.heading("idade", text="idade")
treeview.heading("cidade", text="cidade")

#configurando as colunas
treeview.column("idade", width=50)

#inserindo os ítens
pai = treeview.insert("", "end", values=("majuzinha", "16", "araraquara"))

ttk.Button(janela, text="DELETAR", command=apagar_item).pack()

janela.mainloop()