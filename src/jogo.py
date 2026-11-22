import random

import pygame

from src.config import (
    ALTURA_TELA,
    CAMINHO_RECORDE,
    CHANCE_ACERTO_IA,
    COR_ALERTA,
    COR_FUNDO,
    COR_GRADE,
    COR_HOSTIL,
    COR_INOCENTE,
    COR_JOGADOR,
    COR_TEXTO,
    COR_TIRO,
    DURACAO_PARTIDA,
    FPS,
    INTERVALO_ROBOS,
    LARGURA_TELA,
    PENALIDADE_INOCENTE,
    PONTOS_HOSTIL,
    TAMANHO_JOGADOR,
    TAMANHO_ROBO,
    TITULO_JOGO,
    VELOCIDADE_JOGADOR,
    VELOCIDADE_TIRO,
    VIDAS_INICIAIS,
)
from src.dados import carregar_recorde, salvar_recorde
from src.funcoes import (
    calcular_pontos,
    classificar_robo,
    jogador_perdeu,
    limitar_valor,
    tempo_restante,
)


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


def criar_robo():
    """Cria um robô em uma das bordas da fábrica."""
    lado = random.choice(("cima", "baixo", "esquerda", "direita"))

    if lado == "cima":
        x = random.randint(0, LARGURA_TELA - TAMANHO_ROBO)
        y = 0
    elif lado == "baixo":
        x = random.randint(0, LARGURA_TELA - TAMANHO_ROBO)
        y = ALTURA_TELA - TAMANHO_ROBO
    elif lado == "esquerda":
        x = 0
        y = random.randint(0, ALTURA_TELA - TAMANHO_ROBO)
    else:
        x = LARGURA_TELA - TAMANHO_ROBO
        y = random.randint(0, ALTURA_TELA - TAMANHO_ROBO)

    tipo = random.choice(("hostil", "hostil", "inocente"))
    direcao = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
    if direcao.length_squared() == 0:
        direcao.x = 1

    return {
        "rect": pygame.Rect(x, y, TAMANHO_ROBO, TAMANHO_ROBO),
        "x": float(x),
        "y": float(y),
        "tipo": tipo,
        "classificacao": classificar_robo(tipo, CHANCE_ACERTO_IA),
        "velocidade": random.randint(65, 100) if tipo == "hostil" else random.randint(35, 55),
        "direcao": direcao.normalize(),
    }


def movimentar_robos(robos, jogador, delta):
    """Hostis perseguem o técnico; inocentes circulam pelo cenário."""
    for robo in robos:
        if robo["tipo"] == "hostil":
            direcao = pygame.Vector2(jogador.center) - pygame.Vector2(robo["rect"].center)
            if direcao.length_squared() > 0:
                direcao = direcao.normalize()
        else:
            direcao = robo["direcao"]

        robo["x"] += direcao.x * robo["velocidade"] * delta
        robo["y"] += direcao.y * robo["velocidade"] * delta

        if robo["x"] <= 0 or robo["x"] >= LARGURA_TELA - TAMANHO_ROBO:
            robo["direcao"].x *= -1
        if robo["y"] <= 0 or robo["y"] >= ALTURA_TELA - TAMANHO_ROBO:
            robo["direcao"].y *= -1

        robo["x"] = limitar_valor(robo["x"], 0, LARGURA_TELA - TAMANHO_ROBO)
        robo["y"] = limitar_valor(robo["y"], 0, ALTURA_TELA - TAMANHO_ROBO)
        robo["rect"].topleft = (round(robo["x"]), round(robo["y"]))


def criar_tiro(jogador, destino):
    """Cria um projétil na direção do clique do mouse."""
    origem = pygame.Vector2(jogador.center)
    direcao = pygame.Vector2(destino) - origem

    if direcao.length_squared() == 0:
        return None

    direcao = direcao.normalize()
    return {
        "posicao": origem,
        "velocidade": direcao * VELOCIDADE_TIRO,
        "rect": pygame.Rect(origem.x - 4, origem.y - 4, 8, 8),
    }


def movimentar_tiros(tiros, delta):
    """Move os tiros e remove aqueles que saíram da janela."""
    area_tela = pygame.Rect(0, 0, LARGURA_TELA, ALTURA_TELA)

    for tiro in tiros:
        tiro["posicao"] += tiro["velocidade"] * delta
        tiro["rect"].center = (
            round(tiro["posicao"].x),
            round(tiro["posicao"].y),
        )

    tiros[:] = [tiro for tiro in tiros if area_tela.colliderect(tiro["rect"])]


def verificar_acertos(tiros, robos, pontos):
    """Resolve colisões entre tiros e robôs e atualiza a pontuação."""
    tiros_remover = set()
    robos_remover = set()

    for indice_tiro, tiro in enumerate(tiros):
        for indice_robo, robo in enumerate(robos):
            if indice_robo in robos_remover:
                continue
            if tiro["rect"].colliderect(robo["rect"]):
                pontos = calcular_pontos(
                    pontos,
                    robo["tipo"],
                    PONTOS_HOSTIL,
                    PENALIDADE_INOCENTE,
                )
                tiros_remover.add(indice_tiro)
                robos_remover.add(indice_robo)
                break

    tiros[:] = [tiro for indice, tiro in enumerate(tiros) if indice not in tiros_remover]
    robos[:] = [robo for indice, robo in enumerate(robos) if indice not in robos_remover]
    return pontos


def verificar_dano(jogador, robos, vidas):
    """Retira uma vida quando um robô hostil encosta no técnico."""
    for robo in robos:
        if robo["tipo"] == "hostil" and jogador.colliderect(robo["rect"]):
            robos.remove(robo)
            return vidas - 1
    return vidas


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


def desenhar_robos(tela, robos, fonte):
    """Desenha o tipo real por cor e o palpite informado pela IA."""
    for robo in robos:
        cor = COR_HOSTIL if robo["tipo"] == "hostil" else COR_INOCENTE
        pygame.draw.rect(tela, cor, robo["rect"], border_radius=5)

        if robo["classificacao"] == "hostil":
            texto = "IA: AMEACA"
            cor_texto = COR_ALERTA
        else:
            texto = "IA: SEGURO"
            cor_texto = COR_TEXTO

        imagem = fonte.render(texto, True, cor_texto)
        posicao = imagem.get_rect(center=(robo["rect"].centerx, robo["rect"].top - 9))
        tela.blit(imagem, posicao)


def desenhar_tiros(tela, tiros):
    for tiro in tiros:
        pygame.draw.circle(tela, COR_TIRO, tiro["rect"].center, 4)


def desenhar_interface(tela, fonte, pontos, vidas, restante, recorde):
    texto = fonte.render(
        f"Pontos: {pontos}     Vidas: {vidas}     Tempo: {int(restante + 0.99)}     Recorde: {recorde}",
        True,
        COR_TEXTO,
    )
    tela.blit(texto, (15, 15))


def desenhar_fim(tela, fonte_grande, fonte_normal, estado, pontos):
    """Exibe o resultado da rodada e a opção de reiniciar."""
    camada = pygame.Surface((LARGURA_TELA, ALTURA_TELA), pygame.SRCALPHA)
    camada.fill((0, 0, 0, 190))
    tela.blit(camada, (0, 0))

    titulo = "TURNO CONCLUIDO" if estado == "vitoria" else "PANE TOTAL"
    cor_titulo = COR_INOCENTE if estado == "vitoria" else COR_HOSTIL

    imagem_titulo = fonte_grande.render(titulo, True, cor_titulo)
    tela.blit(imagem_titulo, imagem_titulo.get_rect(center=(LARGURA_TELA // 2, 240)))

    resumo = fonte_normal.render(f"Pontuacao final: {pontos}", True, COR_TEXTO)
    tela.blit(resumo, resumo.get_rect(center=(LARGURA_TELA // 2, 310)))

    instrucao = fonte_normal.render("Pressione R para jogar novamente", True, COR_TEXTO)
    tela.blit(instrucao, instrucao.get_rect(center=(LARGURA_TELA // 2, 355)))


def novo_jogo():
    """Cria os valores iniciais de uma nova rodada."""
    agora = pygame.time.get_ticks()
    return {
        "jogador": criar_jogador(),
        "robos": [],
        "tiros": [],
        "pontos": 0,
        "vidas": VIDAS_INICIAIS,
        "inicio": agora,
        "ultimo_robo": agora,
        "estado": "jogando",
    }


def executar_jogo():
    """Cria a janela e mantém o loop principal do Pygame em execução."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()
    fonte = pygame.font.Font(None, 18)
    fonte_interface = pygame.font.Font(None, 28)
    fonte_grande = pygame.font.Font(None, 58)
    recorde = carregar_recorde(CAMINHO_RECORDE)
    partida = novo_jogo()
    rodando = True

    while rodando:
        delta = relogio.tick(FPS) / 1000

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False
            elif (
                partida["estado"] == "jogando"
                and evento.type == pygame.MOUSEBUTTONDOWN
                and evento.button == 1
            ):
                tiro = criar_tiro(partida["jogador"], evento.pos)
                if tiro is not None:
                    partida["tiros"].append(tiro)
            elif (
                partida["estado"] != "jogando"
                and evento.type == pygame.KEYDOWN
                and evento.key == pygame.K_r
            ):
                partida = novo_jogo()

        agora = pygame.time.get_ticks()
        restante = tempo_restante(partida["inicio"], agora, DURACAO_PARTIDA)

        if partida["estado"] == "jogando":
            teclas = pygame.key.get_pressed()
            movimentar_jogador(partida["jogador"], teclas, delta)

            if agora - partida["ultimo_robo"] >= INTERVALO_ROBOS:
                partida["robos"].append(criar_robo())
                partida["ultimo_robo"] = agora

            movimentar_robos(partida["robos"], partida["jogador"], delta)
            movimentar_tiros(partida["tiros"], delta)
            partida["pontos"] = verificar_acertos(
                partida["tiros"],
                partida["robos"],
                partida["pontos"],
            )
            partida["vidas"] = verificar_dano(
                partida["jogador"],
                partida["robos"],
                partida["vidas"],
            )

            if jogador_perdeu(partida["vidas"]):
                partida["estado"] = "derrota"
            elif restante <= 0:
                partida["estado"] = "vitoria"

            if partida["pontos"] > recorde:
                recorde = partida["pontos"]
                salvar_recorde(CAMINHO_RECORDE, recorde)

        desenhar_cenario(tela)
        desenhar_robos(tela, partida["robos"], fonte)
        desenhar_tiros(tela, partida["tiros"])
        desenhar_jogador(tela, partida["jogador"])
        desenhar_interface(
            tela,
            fonte_interface,
            partida["pontos"],
            partida["vidas"],
            restante,
            recorde,
        )

        if partida["estado"] != "jogando":
            desenhar_fim(
                tela,
                fonte_grande,
                fonte_interface,
                partida["estado"],
                partida["pontos"],
            )
        pygame.display.flip()

    pygame.quit()
