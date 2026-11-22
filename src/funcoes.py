import random


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro dos limites informados."""
    return max(minimo, min(valor, maximo))


def classificar_robo(tipo_real, chance_acerto=0.75):
    """Retorna a classificação da IA, que pode estar incorreta."""
    if random.random() < chance_acerto:
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
