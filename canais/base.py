from abc import ABC, abstractmethod

class CanalComunicacao(ABC):
    def __init__(self, destino):
        self.destino = destino

    @abstractmethod
    def enviar_mensagem(self, mensagem):
        pass
