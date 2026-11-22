def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro dos limites informados."""
    return max(minimo, min(valor, maximo))
