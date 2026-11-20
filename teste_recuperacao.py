
from datetime import datetime
from discord_alert import enviar_alerta, enviar_recuperacao

# Simula respostas sucessivas do mesmo servidor
url = "https://servidor-exemplo.local"

respostas = [
    {"status_code": 200, "online": True},
    {"status_code": 503, "online": False},
    {"status_code": 200, "online": True}
]

estado_anterior = None

for resposta in respostas:
    resultado = {
        "url": url,
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "status_code": resposta["status_code"],
        "tempo_resposta_ms": 150.0,
        "online": resposta["online"]
    }

    online = resultado["online"]

    print(f"\nSite: {url}")
    print(f"Código HTTP simulado: {resultado['status_code']}")

    if estado_anterior is None:
        print("Primeira verificação.")

        if not online:
            enviar_alerta(resultado)

    elif estado_anterior and not online:
        print("Servidor caiu!")
        enviar_alerta(resultado)

    elif not estado_anterior and online:
        print("Servidor recuperado!")
        enviar_recuperacao(resultado)

    else:
        print("Estado não mudou.")

    estado_anterior = online

print("\nTeste de recuperação finalizado!")
