import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton

class ExemploSimples(BaseWidget):

    def __init__(self):
        super(ExemploSimples,self).__init__('ExemploSimples')
        #Definition of the forms fields
        self._nome = ControlText('Nome', 'Default value')
        self._sobrename = ControlText('Sobrenome')
        self._nomeCompleto = ControlText('Nome completo')
        self._button = ControlButton('Pressione o Botão')


#Execute the application
if __name__ == " __main__":
    from pyforms import start_app
    start_app(ExemploSimples)


#É um framework python 3 para desenvolver aplicações que podem operar nos ambientes Desktop GUI, Terminal e Web.
# A biblioteca é composta por três sub-bibliotecas, cada uma implementando a camada responsável por interpretar
# a aplicação Pyforms em cada ambiente diferente: