import tkinter as tk
janela = tk.Tk()
T = tk.Text(janela, height=2, width=30)
T.pack()
T.insert(tk.END, 'Este é um texto\ncom duas linhas\n')
tk.mainloop()

#Linha 3 - É feita uma instância do componente “Text”.
#Linha 5 - É inserido um texto na instância do componente “text”, que será exibido na tela.
# Observe que o texto é separado em duas linhas com o uso do “\n”.