from mensagens.texto import MensagemTexto
from mensagens.video import MensagemVideo
from mensagens.foto import MensagemFoto
from mensagens.arquivo import MensagemArquivo

from canais.whatsapp import WhatsApp
from canais.telegram import Telegram
from canais.facebook import Facebook
from canais.instagram import Instagram

# Criar mensagens
texto = MensagemTexto("Olá!")
video = MensagemVideo("Vídeo aqui", "video.mp4", "mp4", 100)
foto = MensagemFoto("Olha essa!", "foto.jpg", "jpg")
arquivo = MensagemArquivo("Relatório", "relatorio.pdf", "pdf")

# Criar canais
zap = WhatsApp("+551199999999")
tg = Telegram("@telegramuser")
fb = Facebook("usuario.fb")
insta = Instagram("usuario.insta")

# Enviar mensagens
zap.enviar_mensagem(texto)
tg.enviar_mensagem(video)
fb.enviar_mensagem(foto)
insta.enviar_mensagem(arquivo)
