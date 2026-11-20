
import os
from dotenv import load_dotenv

load_dotenv()


def obter_intervalo():
    """Obtém e valida o intervalo de monitoramento."""

    valor = os.getenv("CHECK_INTERVAL", "60")

    try:
        intervalo = int(valor)

        if intervalo <= 0:
            raise ValueError("O intervalo deve ser maior que zero.")

        return intervalo

    except ValueError:
        print("AVISO: Intervalo inválido. Usando 60 segundos.")
        return 60


def validar_webhook():
    """Verifica se o webhook do Discord está configurado."""

    webhook = os.getenv("DISCORD_WEBHOOK_URL", "").strip()

    if not webhook:
        print("ERRO: Webhook do Discord não configurado.")
        return False

    prefixos_validos = (
        "https://discord.com/api/webhooks/",
        "https://discordapp.com/api/webhooks/"
    )

    if not webhook.startswith(prefixos_validos):
        print("ERRO: Formato da URL do webhook inválido.")
        return False

    return True
