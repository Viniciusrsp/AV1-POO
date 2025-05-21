from mensagens.base import Mensagem

class MensagemFoto(Mensagem):
    def __init__(self, conteudo, arquivo, formato):
        super().__init__(conteudo)
        self.arquivo = arquivo
        self.formato = formato

    def exibir(self):
        return f"[Foto] {self.conteudo} | Arquivo: {self.arquivo}, Formato: {self.formato} | Enviado em: {self.data_envio}"
