
import time
import schedule

from monitor import verificar_site
from discord_alert import enviar_alerta, enviar_recuperacao
from config import obter_intervalo, validar_webhook
from historico import salvar_historico

sites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://httpbin.org/status/503"
]

# Obtém o intervalo validado pelo config.py
intervalo = obter_intervalo()

# Guarda o último estado conhecido de cada site
estados_anteriores = {}


def executar_monitoramento():
    print("\n================================")
    print("  INICIANDO VERIFICAÇÃO")
    print("================================")

    for site in sites:
        resultado = verificar_site(site)
        # Registra a verificação em JSON
        salvar_historico(resultado)

        online = resultado["online"]
        estado_anterior = estados_anteriores.get(site)

        print(f"\nSite: {site}")
        print(f"Status: {'ONLINE' if online else 'OFFLINE'}")
        print(f"Código HTTP: {resultado['status_code']}")
        print(f"Tempo: {resultado['tempo_resposta_ms']} ms")

        if "erro" in resultado:
            print(f"Erro: {resultado['erro']}")

        if estado_anterior is None:
            # Primeira verificação
            if not online:
                enviar_alerta(resultado)

        elif estado_anterior and not online:
            # O servidor estava online e ficou offline
            print("Nova falha detectada!")
            enviar_alerta(resultado)

        elif not estado_anterior and online:
            # O servidor estava offline e voltou a funcionar
            print("Servidor recuperado!")
            enviar_recuperacao(resultado)

        # Atualiza o estado conhecido
        estados_anteriores[site] = online

    print("\nVerificação finalizada!")


def main():
    print("================================")
    print("  MONITORAMENTO AUTOMÁTICO")
    print("          DE REDES")
    print("================================")

    print(f"Intervalo configurado: {intervalo} segundos")

    # Verifica a configuração do Discord
    if not validar_webhook():
        print("Monitoramento cancelado: configure o webhook.")
        return

    # Primeira verificação imediata
    executar_monitoramento()

    # Agenda verificações periódicas
    schedule.every(intervalo).seconds.do(executar_monitoramento)

    print("\nMonitoramento ativo. Pressione Ctrl+C para parar.")

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nMonitoramento encerrado pelo usuário.")


if __name__ == "__main__":
    main()
