import tkinter as  tk

#Criando uma janela 
janela = tk.Tk()

#Criando o título
janela.title("hello world")

#mudando a cor da janela
janela.configure(bg="#FACADA")

#colocando ícone 
janela.iconbitmap("watermelon.ico")

#loop para manter a janela aberta
janela.mainloop()