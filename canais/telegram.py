from canais.base import CanalComunicacao

class Telegram(CanalComunicacao):
    def enviar_mensagem(self, mensagem):
        print(f"[Telegram para {self.destino}] {mensagem.exibir()}")
