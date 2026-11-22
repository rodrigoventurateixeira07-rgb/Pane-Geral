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
