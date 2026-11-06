# Guia de artes para Cases de Sucesso Audaces

Padrão consolidado no case **Giadamarina** (nov/2026), a partir das referências
Moda Magia, Primal | Terrablue e Univali. Use este guia como ponto de partida para
os próximos cases.

- Case Giadamarina (Figma): https://www.figma.com/design/ajnYMWhZIiZEmOnUxxqoeM/Case-Giadamarina?node-id=8-11
- Referências e Padrões (Figma): https://www.figma.com/design/GyaCNTxVmORyOqJP1cwIxK/Refer%C3%AAncias-e-Padr%C3%B5es

---

## 1. Antes de começar (checklist de insumos)

- [ ] **Copy aprovada**: título, subtítulo, CTA. A copy não precisa ser seguida à risca na
      arte. Exemplo: o título sempre usa **"Audaces + Cliente"** (com **+**, não "x"), mesmo
      que a copy diga "AUDACES x CLIENTE".
- [ ] **Logo oficial da Audaces** (símbolo branco em vetor). Nunca use logo gerada ou redesenhada.
- [ ] **Fotos/frames do vídeo do cliente**, de preferência **sem legendas gravadas** na imagem.
- [ ] **Vídeo original** (para o Stories animado) e **trilha** (arquivo de música).
- [ ] Qual case é a referência principal. Padrão atual: **Moda Magia**.

## 2. Regras gerais

| Item | Regra |
|---|---|
| Margem padrão | **80px** nas bordas na maioria das artes |
| Margem Stories | **250px em cima e 250px embaixo** |
| Alinhamento | Blocos de texto com **largura fixa** e conteúdo centralizado no eixo da arte. Não deixe o bloco "abraçar" (hug) o título, senão ele sai do centro. |
| Fonte | Inter (título Bold, subtítulo Medium, tag Semi Bold, botão Bold) |
| Título | Inter Bold, entrelinha 95%, espaçamento −2%, branco, 2 linhas: `Audaces +` / `Cliente` |
| Subtítulo | Inter Medium, entrelinha 130%, branco |
| Cor do botão | Laranja `#FF5E00` (nas referências mede ≈ `#FF6700`), texto branco |
| Rosto da pessoa | **Nunca** fica coberto por texto. Se o título no topo cobrir o rosto, desça o bloco de texto para a base. |

### Componentes

- **Tag "STORIA DI SUCCESSO"**: pílula (raio 999), contorno branco 2px, sem preenchimento,
  Inter Semi Bold 22, maiúsculas, espaçamento 6%, padding 26 × 11 → **≈ 292 × 49px** no tamanho base.
- **Botão "SCOPRI LA STORIA"**: Inter Bold 28, padding 36 × 16 → **≈ 342 × 66px**.
  **Raio ≈ 1/3 da altura** (22px para 66px de altura, 26px para 79px). Não use cantos quadrados (12px).
  Ao escalar o botão, recalcule o raio: `raio = altura × 0,33`.

### Degradê (overlay escuro)

- Cor base quase preta (`#0A0A0F`), **nunca preto chapado**.
- Use **muitas paradas (≈10) com curva suave** (smoothstep). Duas ou três paradas deixam o
  degradê "duro".
- O meio da transição fica claro, para a foto aparecer. O escuro forte só aparece **na borda**,
  para dar leitura ao texto e esconder artefatos da foto.
- Opacidade máxima na borda: ≈ 0,90.

## 3. Especificação por formato

| Formato | Logo | Layout | Textos |
|---|---|---|---|
| **ADS 1080×1080** | 50px, centralizado, topo a 80px | Bloco de texto centralizado (largura 864) **na base**, fim a 80px da borda | Tag 49h · Título 84 · Subtítulo 30 · Botão 66h (raio 22) · gap 24 |
| **FEED 1080×1350** | 50px, centralizado, topo a 80px | Igual ao ADS, base a 80px | Igual ao ADS |
| **STORIES 1080×1920** | 79px, centralizado, topo a 250px | Topo: tag + título (início ≈ 413px, gap 36). Base: subtítulo + botão (gap 44), fim a 250px da borda | Tag 67h · Título 112 · Subtítulo 36 · Botão 79h (raio 26) |
| **THUMBNAIL-YOUTUBE 1920×1080** | 58px, centralizado **acima** do bloco (70px de espaço) | Coluna centralizada (largura 760) no lado oposto ao da pessoa, centralizada na vertical | Tag 49h · Título 100 · Subtítulo 34 · **sem botão** · gap 32 |
| **CAPA-LINKEDIN 1920×1080** | **sem logo** | Tag + título alinhados à esquerda, no lado oposto ao da pessoa, centralizados na vertical (gap 40) | Tag 65h · Título 128 · **sem subtítulo e sem botão** |
| **HEADER-E-MAIL 1200×600** | 50px no **canto superior esquerdo** (80, 80) | Bloco **alinhado à direita**, margem direita 80, centralizado na vertical (gap 18) | Tag 33h · Título 68 · Subtítulo 21 · Botão 50h |
| **BANNER-SITE 1080×1350** | sem logo | **Só a foto + fade branco** na base (transparente em 60% da altura, branco total em ~85%) | sem texto, porque ele entra no HTML do site |
| **MINIATURA-LP 1280×780** | sem logo | **Só a foto** | sem texto |

Notas:
- No ADS e no FEED as referências colocam o título no topo. Se a foto tiver o rosto no
  terço superior, mantenha o bloco de texto na base.
- No BANNER-SITE, enquadre a foto de modo que a pessoa termine **antes** do fade branco
  (reposicione/zoom out a imagem se for preciso).
- Textos removidos de um formato devem ser **ocultados**, não apagados, para manter a
  possibilidade de reverter.

## 4. Stories animado (vídeo)

O Figma anima camadas, mas não é editor de vídeo. Ele também não aceita vídeos grandes
(máx. ~100MB). O fluxo que funcionou foi **Figma para a arte + ffmpeg para o vídeo**:

1. **Camadas no Figma**: duplicar o frame STORIES três vezes, sem a foto e sem fundo:
   - `Stories vídeo — gradientes` (só os degradês)
   - `Stories vídeo — topo` (logo + tag + título)
   - `Stories vídeo — base` (subtítulo + botão)

   Exportar cada um como **PNG transparente 1080×1920** (`ov_grad.png`, `ov_top.png`, `ov_bot.png`).
2. **Vídeo original**: baixar o arquivo em resolução máxima. O link do Google Drive precisa
   estar como "qualquer pessoa com o link".
3. **Escolha das cenas**: extrair 1 quadro a cada 2s, montar uma folha de contato e escolher
   cenas de **produto → produção → tecnologia Audaces**. Evitar cenas com rosto no terço superior,
   porque ficam embaixo do título. Para cada cena, definir o segundo inicial e o centro
   horizontal do recorte 9:16 (`shots.txt`).
4. **Música**: o vídeo fica **sem o áudio original, só com a trilha**. Medir o BPM e começar
   num tempo forte (no case Giadamarina: "Kiara" do Bonobo, ≈129 bpm, a partir de 0:59,7).
5. **Cortes no ritmo**: cada cena dura **4 batidas** (≈1,86s), o que dá **8 cenas ≈ 15s**.
   Para 30s, use 16 cenas.
6. **Textos e botão aparecem desde o início** (fade de 0,7s no primeiro segundo) e ficam até o fim.
7. **Saída**: MP4 H.264, 1080×1920, 25fps, AAC 192k, `faststart`. São ≈12MB para 15s.

O script está em [`scripts/render.py`](scripts/render.py) e o exemplo de cenas em
[`scripts/shots.txt`](scripts/shots.txt). Para rodar:

```bash
python3 scripts/render.py
```

O comando roda na pasta com `src.mp4`, `music.mp3`, `shots.txt` e os 3 PNGs. Ajuste
`BEAT`, `MUSIC_START` e `OUT` no topo do script.

## 5. Como pedir para o Claude (para sair certo na primeira vez)

- Envie **referências com camadas** (frames editáveis), não só imagens achatadas. Assim os
  tamanhos são lidos exatamente, sem medição por pixel.
- Informe **qual case é o modelo** e aponte este guia.
- Passe **fotos sem legenda** e o **vídeo original** por link público.
- Para ajustes pontuais, **comente direto no elemento no Figma** ou mande o link do nó.

## 6. Checklist final antes de entregar

- [ ] Logo oficial, no tamanho certo por formato (tabela da seção 3)
- [ ] Título com **+**
- [ ] Margens: 80px (Stories: 250px em cima e embaixo)
- [ ] Todos os blocos centralizados no eixo correto (conferir no zoom)
- [ ] Botão com cantos arredondados (raio ≈ 1/3 da altura)
- [ ] Degradê suave, sem faixa preta "dura"
- [ ] Nenhum texto sobre o rosto da pessoa
- [ ] Sem legendas/artefatos de vídeo aparecendo nas bordas da foto
- [ ] BANNER-SITE com fade branco e MINIATURA-LP só com a foto
