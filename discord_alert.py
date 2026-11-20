
import os
import requests
from dotenv import load_dotenv

load_dotenv()


def enviar_alerta(resultado):
    """Envia um alerta de falha para o Discord."""

    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    if not webhook_url:
        print("ERRO: Webhook do Discord não configurado!")
        return False

    mensagem = {
        "embeds": [
            {
                "title": "🚨 ALERTA DE SERVIDOR",
                "description": "Um site monitorado apresentou uma falha!",
                "color": 15158332,
                "fields": [
                    {
                        "name": "🌐 Site",
                        "value": resultado["url"],
                        "inline": False
                    },
                    {
                        "name": "📡 Código HTTP",
                        "value": str(resultado["status_code"]),
                        "inline": True
                    },
                    {
                        "name": "⏱️ Tempo de resposta",
                        "value": f"{resultado['tempo_resposta_ms']} ms",
                        "inline": True
                    },
                    {
                        "name": "📅 Data e hora",
                        "value": resultado["data_hora"],
                        "inline": False
                    }
                ],
                "footer": {
                    "text": "Monitoramento Automático de Redes"
                }
            }
        ]
    }

    try:
        resposta = requests.post(
            webhook_url,
            json=mensagem,
            timeout=10
        )

        resposta.raise_for_status()

        print("Alerta enviado ao Discord com sucesso!")
        return True

    except requests.exceptions.RequestException as erro:
        status = (
            f" (HTTP {erro.response.status_code})" if erro.response is not None else ""
        )
        print(f"Erro ao enviar alerta: {type(erro).__name__}{status}")
        return False


def enviar_recuperacao(resultado):
    """Envia uma notificação quando um servidor volta a funcionar."""

    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    if not webhook_url:
        print("ERRO: Webhook do Discord não configurado!")
        return False

    mensagem = {
        "embeds": [
            {
                "title": "✅ SERVIDOR RECUPERADO",
                "description": "O site voltou a funcionar normalmente!",
                "color": 3066993,
                "fields": [
                    {
                        "name": "🌐 Site",
                        "value": resultado["url"],
                        "inline": False
                    },
                    {
                        "name": "📡 Código HTTP",
                        "value": str(resultado["status_code"]),
                        "inline": True
                    },
                    {
                        "name": "⏱️ Tempo de resposta",
                        "value": f"{resultado['tempo_resposta_ms']} ms",
                        "inline": True
                    },
                    {
                        "name": "📅 Data e hora",
                        "value": resultado["data_hora"],
                        "inline": False
                    }
                ],
                "footer": {
                    "text": "Monitoramento Automático de Redes"
                }
            }
        ]
    }

    try:
        resposta = requests.post(
            webhook_url,
            json=mensagem,
            timeout=10
        )

        resposta.raise_for_status()

        print("Recuperação enviada ao Discord com sucesso!")
        return True

    except requests.exceptions.RequestException as erro:
        status = (
            f" (HTTP {erro.response.status_code})" if erro.response is not None else ""
        )
        print(f"Erro ao enviar recuperação: {type(erro).__name__}{status}")
        return False
