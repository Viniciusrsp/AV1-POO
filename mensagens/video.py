from mensagens.base import Mensagem

class MensagemVideo(Mensagem):
    def __init__(self, conteudo, arquivo, formato, duracao):
        super().__init__(conteudo)
        self.arquivo = arquivo
        self.formato = formato
        self.duracao = duracao

    def exibir(self):
        return f"[Vídeo] {self.conteudo} | Arquivo: {self.arquivo}, Formato: {self.formato}, Duração: {self.duracao}s | Enviado em: {self.data_envio}"
