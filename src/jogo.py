import pygame

from src.config import (
    ALTURA_TELA,
    COR_FUNDO,
    COR_GRADE,
    COR_JOGADOR,
    FPS,
    LARGURA_TELA,
    TAMANHO_JOGADOR,
    TITULO_JOGO,
    VELOCIDADE_JOGADOR,
)
from src.funcoes import limitar_valor


def criar_jogador():
    """Cria o técnico no centro da fábrica."""
    x = LARGURA_TELA // 2 - TAMANHO_JOGADOR // 2
    y = ALTURA_TELA // 2 - TAMANHO_JOGADOR // 2
    return pygame.Rect(x, y, TAMANHO_JOGADOR, TAMANHO_JOGADOR)


def movimentar_jogador(jogador, teclas, delta):
    """Move o jogador pelas setas ou por WASD sem sair da tela."""
    direcao = pygame.Vector2(0, 0)

    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        direcao.x -= 1
    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        direcao.x += 1
    if teclas[pygame.K_w] or teclas[pygame.K_UP]:
        direcao.y -= 1
    if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
        direcao.y += 1

    if direcao.length_squared() > 0:
        direcao = direcao.normalize()
        jogador.x += round(direcao.x * VELOCIDADE_JOGADOR * delta)
        jogador.y += round(direcao.y * VELOCIDADE_JOGADOR * delta)

    jogador.x = limitar_valor(jogador.x, 0, LARGURA_TELA - jogador.width)
    jogador.y = limitar_valor(jogador.y, 0, ALTURA_TELA - jogador.height)


def desenhar_cenario(tela):
    """Desenha um chão industrial provisório para a fábrica."""
    tela.fill(COR_FUNDO)

    for x in range(0, LARGURA_TELA, 80):
        pygame.draw.line(tela, COR_GRADE, (x, 0), (x, ALTURA_TELA))

    for y in range(0, ALTURA_TELA, 80):
        pygame.draw.line(tela, COR_GRADE, (0, y), (LARGURA_TELA, y))


def desenhar_jogador(tela, jogador):
    """Representa provisoriamente o técnico com um quadrado azul."""
    pygame.draw.rect(tela, COR_JOGADOR, jogador, border_radius=7)
    pygame.draw.circle(tela, (245, 245, 245), jogador.center, 5)


def executar_jogo():
    """Cria a janela e mantém o loop principal do Pygame em execução."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()
    jogador = criar_jogador()
    rodando = True

    while rodando:
        delta = relogio.tick(FPS) / 1000

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False

        teclas = pygame.key.get_pressed()
        movimentar_jogador(jogador, teclas, delta)

        desenhar_cenario(tela)
        desenhar_jogador(tela, jogador)
        pygame.display.flip()

    pygame.quit()
