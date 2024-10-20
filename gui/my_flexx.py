#É um kit de ferramentas para o desenvolvimento de interfaces gráficas com o usuário implementado em python
# que faz uso de tecnologia web para sua renderização. O Flexx pode ser usado para criar tanto aplicações de
# desktop como para web e até mesmo exportar uma aplicação para um documento HTML independente.
# Para instalar o Flexx, basta digitar o comando:

from flexx import flx
class Exemplo(flx.Widget):

    def init(self):
        flx.Button(text='Olá')
        flx.Button(text='Mundo')


if __name__ == "__main__":
    a = flx.App(Exemplo,title='Flexx Demonstração')
    m = a.launch()
    flx.run()

