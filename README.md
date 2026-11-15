# Pane Geral

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Rodrigo Ventura
- Daniel Costa
- Daniel Viana
- Felipe Custodio

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

Pane Geral é um jogo arcade de sobrevivência com visão superior. Em uma fábrica automatizada em emergência, o jogador controla um técnico e precisa distinguir robôs hostis de robôs de manutenção inocentes. Um sistema de IA tenta classificá-los, mas pode errar, colocando em questão a confiabilidade de decisões automatizadas e a necessidade de supervisão humana.

## Objetivo do jogador

Sobreviver por 60 segundos com pelo menos uma das três vidas, neutralizando robôs hostis e evitando atingir robôs inocentes para alcançar a maior pontuação possível.

## Regras do jogo

- O jogador começa com três vidas.
- A rodada dura 60 segundos.
- Acertar um robô hostil soma pontos.
- Acertar um robô inocente desconta pontos.
- A classificação automática pode estar errada e deve ser avaliada pelo jogador.
- Ataques ou colisões com robôs hostis retiram vidas.
- Sobreviver até o fim do tempo conclui a rodada; perder todas as vidas causa derrota.

## Controles

- W, A, S e D ou setas: movimentar o técnico
- Mouse: mirar
- Botão esquerdo do mouse: atirar
- Esc: sair do jogo

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd Pane-Geral
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.md` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
