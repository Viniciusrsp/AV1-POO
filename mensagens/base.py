from abc import ABC, abstractmethod
from datetime import datetime

class Mensagem(ABC):
    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.data_envio = datetime.now()

    @abstractmethod
    def exibir(self):
        pass
