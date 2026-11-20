
import requests
from datetime import datetime


def verificar_site(url):
    """Verifica a disponibilidade e o tempo de resposta de um site."""

    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    try:
        resposta = requests.get(url, timeout=5)

        status_code = resposta.status_code
        tempo_resposta = round(resposta.elapsed.total_seconds() * 1000, 2)

        online = 200 <= status_code < 400

        resultado = {
            "url": url,
            "data_hora": data_hora,
            "status_code": status_code,
            "tempo_resposta_ms": tempo_resposta,
            "online": online
        }

    except requests.exceptions.RequestException as erro:
        resultado = {
            "url": url,
            "data_hora": data_hora,
            "status_code": None,
            "tempo_resposta_ms": None,
            "online": False,
            "erro": str(erro)
        }

    return resultado
