from canais.base import CanalComunicacao

class WhatsApp(CanalComunicacao):
    def enviar_mensagem(self, mensagem):
        print(f"[WhatsApp para {self.destino}] {mensagem.exibir()}")
