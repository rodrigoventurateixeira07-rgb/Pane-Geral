import random


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro dos limites informados."""
    return max(minimo, min(valor, maximo))


def classificar_robo(tipo_real, chance_acerto=0.75, sorteio=None):
    """Retorna a classificação da IA, que pode estar incorreta."""
    valor = random.random() if sorteio is None else sorteio
    if valor < chance_acerto:
        return tipo_real

    if tipo_real == "hostil":
        return "inocente"
    return "hostil"


def calcular_pontos(pontos, tipo_robo, premio=10, penalidade=10):
    """Soma pontos por hostil e desconta por inocente atingido."""
    if tipo_robo == "hostil":
        return pontos + premio
    return pontos - penalidade


def jogador_perdeu(vidas):
    """Indica quando o técnico ficou sem vidas."""
    return vidas <= 0


def tempo_restante(inicio_ms, agora_ms, duracao_segundos=60):
    """Calcula quantos segundos ainda faltam para terminar a rodada."""
    tempo_decorrido = (agora_ms - inicio_ms) / 1000
    return max(0, duracao_segundos - tempo_decorrido)
