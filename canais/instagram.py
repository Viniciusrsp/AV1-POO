from canais.base import CanalComunicacao

class Instagram(CanalComunicacao):
    def enviar_mensagem(self, mensagem):
        print(f"[Instagram para @{self.destino}] {mensagem.exibir()}")
