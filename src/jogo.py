import pygame

from src.config import (
    ALTURA_TELA,
    COR_FUNDO,
    COR_GRADE,
    FPS,
    LARGURA_TELA,
    TITULO_JOGO,
)


def desenhar_cenario(tela):
    """Desenha um chão industrial provisório para a fábrica."""
    tela.fill(COR_FUNDO)

    for x in range(0, LARGURA_TELA, 80):
        pygame.draw.line(tela, COR_GRADE, (x, 0), (x, ALTURA_TELA))

    for y in range(0, ALTURA_TELA, 80):
        pygame.draw.line(tela, COR_GRADE, (0, y), (LARGURA_TELA, y))


def executar_jogo():
    """Cria a janela e mantém o loop principal do Pygame em execução."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()
    rodando = True

    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False

        desenhar_cenario(tela)
        pygame.display.flip()

    pygame.quit()
