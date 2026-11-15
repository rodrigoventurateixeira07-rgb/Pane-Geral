# Proposta Inicial do Jogo — Pane Geral

## 1. Nome provisório do jogo

**Nome:** Pane Geral

O nome faz referência tanto às falhas que tomam conta da fábrica quanto ao problema central do jogo: um sistema automatizado que nem sempre consegue distinguir corretamente uma ameaça.

## 2. Integrantes do grupo

- Rodrigo Ventura
- Daniel Costa
- Daniel Viana
- Felipe Custodio

## 3. Tema escolhido

**Tema:** Inteligência artificial responsável: confiabilidade de sistemas de classificação automatizada e necessidade de supervisão humana.

**Como esse tema se relaciona com o jogo?**

O sistema de segurança da fábrica usa uma classificação automatizada para marcar robôs como hostis ou inocentes, mas pode cometer erros. O jogador precisa observar os robôs antes de atirar, pois atingir um robô inocente reduz a pontuação. Assim, a falha da IA interfere diretamente nas decisões, regras e resultados da partida, mostrando que decisões automatizadas não devem ser aceitas sem análise humana.

**Uso responsável e reflexão proposta:**

O jogo não apresenta a IA como infalível nem incentiva a delegação total de decisões a ela. A classificação serve como apoio, enquanto a decisão final cabe ao jogador. A proposta busca provocar uma reflexão sobre falsos positivos, consequências de classificações incorretas, transparência, responsabilidade e a importância de supervisão humana em sistemas automatizados.

## 4. Tipo de jogo

**Tipo escolhido:** Jogo arcade de ação e sobrevivência com visão superior (top-down).

## 5. Descrição geral do jogo

Pane Geral acontece em uma fábrica automatizada que entrou em estado de emergência. O jogador controla um técnico visto de cima, deslocando-se pelo chão da fábrica enquanto robôs aparecem e circulam pelo cenário. Alguns são hostis e atacam o técnico; outros são robôs de manutenção inocentes. Um sistema automático tenta classificá-los, mas seus alertas podem estar errados. O jogador deve sobreviver, evitar ataques e disparar apenas contra ameaças reais.

## 6. Objetivo do jogador

Sobreviver por 60 segundos com pelo menos uma vida, neutralizando robôs hostis para obter a maior pontuação possível e evitando atingir robôs inocentes.

## 7. Regras principais

1. O jogador começa cada partida com três vidas e pode se mover em quatro direções.
2. A partida tem duração máxima de 60 segundos.
3. Acertar um robô hostil soma pontos; acertar um robô inocente desconta pontos.
4. O sistema de classificação exibe uma indicação sobre cada robô, mas essa indicação pode estar incorreta, exigindo atenção e julgamento do jogador.
5. Encostar em um robô hostil ou ser atingido por seu ataque retira uma vida; a partida termina se as três vidas forem perdidas.

## 8. Condição de vitória

O jogador conclui e vence a rodada ao permanecer vivo até o cronômetro chegar a zero. A pontuação final representa seu desempenho, premiando ameaças neutralizadas e decisões cuidadosas.

## 9. Condição de derrota ou encerramento

A derrota ocorre quando o jogador perde as três vidas antes do fim dos 60 segundos. A partida também pode ser encerrada voluntariamente pela tecla Esc ou ao fechar a janela.

## 10. Elementos previstos no jogo

- **Personagem ou elemento principal:** técnico da fábrica controlado pelo jogador, visto de cima.
- **Obstáculos ou desafios:** robôs hostis, ataques, movimentação dos robôs, limites do cenário e alertas automatizados falíveis.
- **Itens ou objetos de interação:** projéteis disparados pelo técnico e sinais visuais de classificação; itens de recuperação ficam fora do escopo mínimo.
- **Pontuação, vidas, tempo ou progresso:** pontuação por decisões, três vidas e cronômetro regressivo de 60 segundos.
- **Personagens não hostis:** robôs de manutenção inocentes, que não devem ser atingidos.

## 11. Controles previstos

- **W, A, S e D ou setas direcionais:** mover o técnico para cima, esquerda, baixo e direita.
- **Mouse:** apontar a direção do disparo.
- **Botão esquerdo do mouse:** atirar.
- **Esc:** sair da partida.

## 12. Organização inicial do código

- `main.py`: ponto de entrada do programa.
- `src/jogo.py`: loop principal, eventos, atualização dos estados e desenho da tela.
- `src/config.py`: dimensões, cores, FPS, título e caminhos usados no projeto.
- `src/funcoes.py`: regras e funções auxiliares testáveis, como pontuação, dano, tempo e fim de jogo.
- `src/sprites.py`: carregamento e preparação das imagens.
- `src/dados.py`: leitura e gravação do recorde ou ranking.
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos de pontuação persistente.
- `tests/`: testes das regras principais.

Essa estrutura poderá receber funções ou módulos adicionais somente quando forem necessários, mantendo cada arquivo com uma responsabilidade clara.

## 13. Recursos previstos

- Python e biblioteca Pygame.
- Sprites simples para o técnico, robô hostil, robô inocente, projéteis e cenário industrial.
- Fonte legível para pontuação, vidas, cronômetro e mensagens do sistema.
- Efeitos sonoros curtos para disparo, acerto, dano e fim de partida, caso haja tempo.
- Arquivo de texto para armazenar recorde ou ranking local.
- GitHub para versionamento e colaboração do grupo.

Todos os recursos externos eventualmente utilizados terão sua origem e licença registradas. O grupo dará preferência a recursos próprios, livres ou disponibilizados pelo professor.

## 14. Principais dificuldades esperadas

1. Programar disparos, colisões e movimentação de vários robôs sem tornar o código confuso.
2. Criar uma classificação falível que seja compreensível e equilibrada, sem parecer aleatória demais para o jogador.
3. Controlar corretamente o cronômetro, as três vidas, a pontuação e as condições de encerramento.

## 15. Escopo mínimo para a entrega final

A versão mínima terá uma única arena vista de cima, um técnico que se move e atira, dois tipos visuais de robô (hostil e inocente), classificação automática ocasionalmente incorreta, pontuação, três vidas e cronômetro de 60 segundos. Robôs hostis causarão dano, enquanto disparos em inocentes retirarão pontos. Haverá telas ou mensagens simples de vitória e derrota e o jogo poderá ser reiniciado. O foco será uma rodada curta, completa e funcional, sem fases, narrativa extensa ou sistemas complexos.

## 16. Possíveis melhorias, caso haja tempo

1. Adicionar menu inicial, tutorial curto, efeitos sonoros e animações.
2. Incluir níveis de dificuldade, novos padrões de movimento e diferentes taxas de erro da classificação.
3. Criar ranking local e uma tela final com resumo de acertos, falsos positivos e robôs inocentes preservados.

## 17. Declaração de originalidade

Declaramos que Pane Geral é uma proposta original desenvolvida pelo grupo para a disciplina. O conceito, as regras, a integração do tema de inteligência artificial e o código serão produzidos pelos integrantes. Caso sejam utilizados recursos, referências ou trechos permitidos de terceiros, suas fontes e licenças serão identificadas, e o grupo compreenderá e será capaz de explicar todo o conteúdo entregue.
