from src.funcoes import (
    calcular_pontos,
    classificar_robo,
    jogador_perdeu,
    limitar_valor,
    tempo_restante,
)


def test_pontos_por_robo_hostil():
    assert calcular_pontos(20, "hostil") == 30


def test_penalidade_por_robo_inocente():
    assert calcular_pontos(20, "inocente") == 10


def test_ia_mantem_tipo_quando_acerta():
    assert classificar_robo("hostil", chance_acerto=0.75, sorteio=0.2) == "hostil"


def test_ia_inverte_tipo_quando_erra():
    assert classificar_robo("hostil", chance_acerto=0.75, sorteio=0.9) == "inocente"


def test_limites_de_valor():
    assert limitar_valor(-5, 0, 100) == 0
    assert limitar_valor(50, 0, 100) == 50
    assert limitar_valor(150, 0, 100) == 100


def test_condicao_de_derrota():
    assert jogador_perdeu(0) is True
    assert jogador_perdeu(1) is False


def test_cronometro():
    assert tempo_restante(1000, 11000, 60) == 50
    assert tempo_restante(1000, 70000, 60) == 0
