
import json
from pathlib import Path

# Caminho do arquivo de histórico
CAMINHO_HISTORICO = Path(__file__).resolve().parent / "data" / "historico.json"


def salvar_historico(resultado):
    """Salva o resultado de uma verificação em JSON."""

    try:
        # Garante que a pasta data exista
        CAMINHO_HISTORICO.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        # Carrega o histórico existente
        if CAMINHO_HISTORICO.exists():
            with open(CAMINHO_HISTORICO, "r", encoding="utf-8") as arquivo:
                historico = json.load(arquivo)
        else:
            historico = []

        if not isinstance(historico, list):
            raise ValueError("O histórico deve conter uma lista JSON.")

        # Adiciona a nova verificação
        historico.append(resultado)

        # Salva o histórico atualizado
        with open(CAMINHO_HISTORICO, "w", encoding="utf-8") as arquivo:
            json.dump(
                historico,
                arquivo,
                indent=4,
                ensure_ascii=False
            )

        print("Histórico atualizado com sucesso!")

    except (OSError, ValueError, json.JSONDecodeError) as erro:
        print(f"Erro ao salvar histórico: {erro}")
