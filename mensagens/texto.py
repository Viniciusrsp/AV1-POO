from mensagens.base import Mensagem

class MensagemTexto(Mensagem):
    def exibir(self):
        return f"[Texto] {self.conteudo} | Enviado em: {self.data_envio}"
