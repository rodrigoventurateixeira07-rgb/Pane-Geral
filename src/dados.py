def carregar_recorde(caminho):
    """Carrega o recorde ou retorna zero quando não existe valor válido."""
    try:
        return int(caminho.read_text(encoding="utf-8").strip())
    except (FileNotFoundError, ValueError):
        return 0


def salvar_recorde(caminho, pontuacao):
    """Salva a maior pontuação da partida."""
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(str(pontuacao), encoding="utf-8")
