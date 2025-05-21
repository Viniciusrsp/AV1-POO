from canais.base import CanalComunicacao

class Facebook(CanalComunicacao):
    def enviar_mensagem(self, mensagem):
        print(f"[Facebook para @{self.destino}] {mensagem.exibir()}")
