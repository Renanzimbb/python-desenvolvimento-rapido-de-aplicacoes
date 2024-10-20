import tkinter
from tkinter import ttk
janela = tkinter.Tk()
janela.title('Teste')
#janela.resizable(False,False)

#Widget Label
ttk.Label(janela,text='Componente Label').grid(column=0,row=0)


janela.mainloop()


# Linha 1 - É feita a importação da biblioteca Tkinter.
# Linha 2 - É criada uma instância da classe Tk no objeto “janela”.
# Linha 3 - O método “title” é usado para definir um título que aparece no topo da janela, no caso, “Aplicação GUI”.
# Linha 4 - A aplicação inicia o loop de evento principal da janela.