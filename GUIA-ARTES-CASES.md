# Guia de artes para Cases de Sucesso Audaces

> **Para a IA que vai executar o próximo case: leia este arquivo inteiro antes de qualquer
> chamada ao Figma.** Ele foi escrito depois do case **Giadamarina** (nov/2026), em que a
> primeira entrega veio com vários erros: logo errada, texto descentralizado, botão quadrado,
> degradê duro e formatos fora do padrão. Tudo o que foi corrigido está registrado aqui.
> Seguir este guia é obrigatório. Ele vale mais do que a sua intuição de design.

---

## 0. Fluxo obrigatório (resumo)

1. Ler este guia inteiro.
2. Abrir as **referências** (seção 2) e o **último case pronto** (seção 3). Fazer screenshot
   dos formatos em tamanho real e **medir** (logo, tag, título, botão, margens) com
   [`scripts/medir_referencia.py`](scripts/medir_referencia.py). Não estime a olho.
3. **Partir do último case pronto como template**: duplicar o frame de formatos e trocar
   foto e copy. Não criar do zero, porque foi do zero que vieram os erros do início.
4. Aplicar a copy com as adaptações da seção 4 (ex.: "+" no lugar de "x").
5. Conferir **cada formato** com a tabela da seção 5 e o checklist da seção 9 antes de entregar.
6. Entregar com screenshot e listar o que foi decidido por julgamento (ex.: "texto na base
   para não cobrir o rosto").

---

## 1. Erros cometidos no início do case Giadamarina (não repetir)

| # | Erro | Correção / regra |
|---|---|---|
| 1 | Usei uma **logo gerada** (círculo + "A" desenhado) | Usar **sempre a logo oficial em vetor** (símbolo branco). Ver seção 3. Nunca desenhar ou gerar logo. |
| 2 | **Mesma logo de 80px** em todos os formatos | Cada formato tem um tamanho (seção 5): 50px no feed/ads, 79px no stories, 58px no thumbnail, nenhuma no LinkedIn. |
| 3 | **Texto descentralizado** | Bloco de texto em auto-layout com largura em **HUG** encolhia junto com o título e saía do eixo. Regra: blocos com **largura FIXA** (ex.: 864px = 1080 − 2×108), conteúdo centralizado (`counterAxisAlignItems = CENTER`), posição x calculada. |
| 4 | **Botão quadrado** (raio 12 em 75px de altura) | Raio ≈ **1/3 da altura** (22px para 66px de altura, 26px para 79px). |
| 5 | **Degradê duro e escuro demais** (2–3 paradas, até 97% de preto) | ~10 paradas em curva suave, meio claro e escuro só na borda. Ver seção 6. |
| 6 | **"Audaces x Cliente"** igual à copy | Sempre **"Audaces + Cliente"**, como nas outras artes. |
| 7 | **Margens erradas** | **80px** na maioria das artes; **Stories 250px em cima e embaixo**. Isso vale mais que as referências antigas (Moda Magia tem 45px e 280px). |
| 8 | Todos os formatos com o **mesmo layout** | BANNER-SITE é só foto + fade branco. MINIATURA-LP é só foto. LinkedIn é só tag + título. E-mail tem logo no canto e texto à direita. |
| 9 | Placeholder "Nome do Cliente" / "Breve descrizione..." | Substituir todos os textos. Procurar por placeholders antes de entregar. |
| 10 | **Legenda do vídeo gravada na foto** ("tanti altri brand") apareceu quando o degradê ficou mais claro | Conferir as bordas da foto; reenquadrar (`imageTransform`) ou trocar o frame. |
| 11 | Título no topo **cobrindo o rosto** | Se o rosto está no terço superior, o bloco de texto vai para a base. O rosto nunca fica sob texto. |
| 12 | Artes feitas em **Inter** | Fontes oficiais: **Sora** (título) e **Poppins** (demais textos). Ver seção 5.1. |

---

## 2. Referências existentes

### 2.1 Arquivo "Referências e Padrões" (Figma)

- URL: https://www.figma.com/design/GyaCNTxVmORyOqJP1cwIxK/Refer%C3%AAncias-e-Padr%C3%B5es
- fileKey: `GyaCNTxVmORyOqJP1cwIxK`. Página `Page 1`, frame-mãe **"Cases Referencias"** (`3:33`).
- **Atenção: todas as artes são IMAGENS achatadas** (retângulo com image fill), sem camadas.
  Para tirar medidas exatas: `get_screenshot` com `maxDimension` = maior lado do frame (escala 1x),
  baixar o PNG e medir com `scripts/medir_referencia.py`.

| Case | Frame | Formatos (nodeId) | Observações |
|---|---|---|---|
| **Moda Magia** (Itália) | `1:18` | THUMBNAIL-YOUTUBE `1:10` · Story sem fundo `1:12` · ADS `1:13` · FEED `1:14` · CAPA-LINKEDIN `1:15` · BANNER-SITE `1:16` · STORIES `1:17` | **Referência principal** de layout para cases italianos. |
| **Primal \| Terrablue** (Itália) | `5:10` | ADS `5:11` · BANNER-SITE `5:12` · CAPA-LINKEDIN `5:13` · FEED `5:14` · STORIES `5:15` · THUMBNAIL `5:16` | Mesmo padrão da Moda Magia; confirma banner com fade branco e LinkedIn só com tag + título. |
| **Italfodere** (Itália) | `5:17` | THUMBNAIL-1 `5:18` · THUMBNAIL-5 `5:19` | Só thumbnails: tag + título centralizados, sem logo, overlay escuro do lado do texto. |
| **Univali** (Brasil) | `5:2` | ADS `5:3` · CAPA-LINKEDIN `5:4` · FEED-WHATSAPP `5:5` · HEADER-E-MAIL `5:6` · MINIATURA-LP `5:7` · STORIES-ADS-1 `5:8` · STORIES-ADS-2 `5:9` | **Estilo Brasil**: copy em português, "Case de Sucesso" em texto (sem pílula), botão **azul** "ASSISTA AGORA", logo com palavra "AUDACES" em alguns formatos. Use como referência de **posição** (e-mail, miniatura), não de cor, para cases italianos. |

Medidas já tiradas da Moda Magia (base 1080 de largura):

- ADS e FEED: logo 50×50, tag ≈311×49, título ≈84px, subtítulo ≈30px (3 linhas), botão 346×67 com raio ≈21.
- STORIES: logo 79×79, tag ≈425×67, título ≈112px, subtítulo ≈36px, botão 408×79 com raio ≈25.
- THUMBNAIL 1920×1080: logo 58, tag ≈311×49, título ≈97px, coluna centralizada no lado oposto ao da pessoa.
- CAPA-LINKEDIN 1920×1080: tag ≈392×65, título ≈128px, alinhado à esquerda, sem logo, subtítulo e botão.
- Cor do botão medida: `#FF6700`.

### 2.2 Pasta "Cases" (Figma), com os cases já entregues

Os cases prontos **não ficam na página de referências**: cada um é um arquivo próprio na
**pasta (projeto) "Cases" do Figma**. Eles são a melhor referência, porque têm **camadas
editáveis** (tamanhos exatos e componentes).

- As ferramentas do Figma disponíveis à IA **não listam pastas/projetos**. **Peça ao usuário
  os links** dos cases da pasta "Cases" que ele quer usar como base.
- Case conhecido:

| Case | URL | Frame de formatos |
|---|---|---|
| **Giadamarina** (nov/2026) | https://www.figma.com/design/ajnYMWhZIiZEmOnUxxqoeM/Case-Giadamarina?node-id=8-11 | `8:11` "Novo Case — Formatos" |

---

## 3. Estrutura do case Giadamarina (template)

fileKey `ajnYMWhZIiZEmOnUxxqoeM`, página `Page 1`.

| Elemento | nodeId | Notas |
|---|---|---|
| Frame com todos os formatos | `8:11` | Duplicar este frame para um novo case |
| ADS 1080×1080 | `8:12` | |
| FEED 1080×1350 | `8:27` | |
| BANNER-SITE 1080×1350 | `8:42` | Bloco de texto e degradês ocultos; retângulo "Fade branco" |
| STORIES 1080×1920 | `8:55` | |
| THUMBNAIL-YOUTUBE 1920×1080 | `8:71` | |
| CAPA-LINKEDIN 1920×1080 | `8:84` | Logo, subtítulo e botão ocultos |
| HEADER-E-MAIL 1200×600 | `8:99` | |
| MINIATURA-LP 1280×780 | `8:114` | Bloco de texto e degradês ocultos |
| Componente **Tag / Storia di successo** | `8:7` | |
| Componente **Botão CTA** | `8:9` | |
| **Logo oficial Audaces** (símbolo branco, vetor) | `13:40` "Logo simbolo_white 1" | **Fonte da logo.** Clonar e usar `rescale()`; não usar instância gerada. |
| Camadas do Stories em vídeo | `24:14` gradientes · `24:28` topo · `24:42` base | PNG transparente para o vídeo (seção 7) |

Camadas de cada formato: `Foto` (image fill, `scaleMode: CROP`), `Gradiente` (1 ou 2 retângulos),
`Logo Audaces`, `Conteúdo` (auto-layout vertical: tag, `Título`, `Subtítulo`, botão).

---

## 4. Copy: como adaptar

- A copy chega em italiano (blocos LP / TYP / ADS). **As artes usam o bloco ADS**:
  - título: **"Audaces +" / "Cliente"** em 2 linhas, Title Case. Nunca usar "x" e nunca caixa alta, mesmo que a copy venha assim;
  - subtítulo: a frase do ADS, quebrada em 2 linhas equilibradas (ex.: "La tradizione Made in Italy evolve / con l'automazione.");
  - CTA: **"SCOPRI LA STORIA"**;
  - tag: **"STORIA DI SUCCESSO"**.
- "Não precisa seguir à risca": priorize a consistência com as outras artes do case.
- LP, TYP, título SEO e meta description **não fazem parte das artes**. Só crie telas de LP
  se o usuário pedir explicitamente.

---

## 5. Especificação por formato

Regras gerais: margem **80px** (Stories: **250px** em cima e embaixo). Fontes oficiais dos cases: **Sora** (títulos) e **Poppins** (demais textos). Ver seção 5.1.

| Formato | Logo | Layout | Textos (px) |
|---|---|---|---|
| **ADS 1080×1080** | 50, centralizado, topo y=80 | Bloco centralizado, largura fixa 864 (x=108), **na base**, terminando em y=1000 | Tag h49 · Título 84 · Subtítulo 30 · Botão h66 (raio 22) · gap 24 |
| **FEED 1080×1350** | 50, centralizado, topo y=80 | Igual ao ADS, terminando em y=1270 | Igual ao ADS |
| **STORIES 1080×1920** | 79, centralizado, topo y=250 | Topo: tag + título, largura 864, início y≈413, gap 36. Base: subtítulo + botão, largura 864, gap 44, terminando em y=1670 | Tag h67 · Título 112 · Subtítulo 36 · Botão h79 (raio 26) |
| **THUMBNAIL-YOUTUBE 1920×1080** | 58, centralizado sobre o bloco, 70px acima da tag | Coluna largura 760, **texto centralizado**, no lado oposto ao da pessoa (Giadamarina: x=1025), centralizada na vertical | Tag h49 · Título 100 · Subtítulo 34 · **sem botão** · gap 32 |
| **CAPA-LINKEDIN 1920×1080** | **nenhuma** | Tag + título **alinhados à esquerda**, lado oposto ao da pessoa (x=1030), centralizados na vertical, gap 40 | Tag h65 · Título 128 · **sem subtítulo e sem botão** |
| **HEADER-E-MAIL 1200×600** | 50, canto superior esquerdo (80, 80) | Bloco **alinhado à direita** (`counterAxisAlignItems = MAX`, texto `RIGHT`), largura 520, borda direita em x=1120, centralizado na vertical, gap 18 | Tag h33 · Título 68 · Subtítulo 21 · Botão h50 |
| **BANNER-SITE 1080×1350** | nenhuma | **Só foto + fade branco** na base (o texto vai no HTML do site). A pessoa precisa terminar antes do fade: reenquadrar com zoom out se for preciso | — |
| **MINIATURA-LP 1280×780** | nenhuma | **Só a foto**, sem degradê | — |

Notas de julgamento:
- **ADS/FEED**: as referências põem o título no topo. Se o rosto estiver no terço superior
  da foto, todo o bloco de texto vai para a base e só a logo fica no topo.
- Elementos que não pertencem ao formato devem ser **ocultados** (`visible = false`), não apagados.

### Componentes

| Componente | Especificação |
|---|---|
| **Tag** | Pílula (raio 999), contorno branco 2px, sem preenchimento, Poppins **Medium 22**, maiúsculas, espaçamento 6%, padding 26×11 → ≈292×49 |
| **Botão** | Preenchimento laranja `#FF5E00` (referência mede `#FF6700`), Poppins **SemiBold 28** branco, espaçamento 2%, padding 36×16 → ≈342×66, **raio 22** |
| **Título** | **Sora Bold**, entrelinha 95%, espaçamento −2%, branco |
| **Subtítulo** | **Poppins Medium**, entrelinha 130%, branco |

### 5.1 Fontes

- **Fontes oficiais dos cases: Sora e Poppins** (definição do time de marketing). Não use Inter.
- Divisão adotada: **Sora** no título ("Audaces + Cliente"); **Poppins** no subtítulo, na tag e
  no botão. Os pesos estão na tabela de componentes acima.
- Nomes exatos no Figma (sem espaço): Sora `Bold`/`SemiBold`/`ExtraBold`; Poppins `Medium`/`SemiBold`/`Bold`.
  Sempre `await figma.loadFontAsync(...)` antes de editar.
- O case Giadamarina (nov/2026) foi entregue em **Inter**, antes dessa definição. Não copie a fonte dele.
  Ao duplicar o template, troque as fontes.
- Ao trocar a fonte, a largura do título muda. Confira se o título ainda cabe com a margem e
  se o bloco continua centralizado.

Ao escalar tag ou botão para outro formato, use `instance.rescale(alturaAlvo / alturaAtual)` e,
no botão, ajuste depois `cornerRadius = round(altura × 0,33)`.

---

## 6. Degradê (overlay)

- Cor base `#0A0A0F` (quase preto, nunca preto puro).
- Gradiente linear com **~10 paradas** em curva suave (smoothstep). Exemplo para "escuro embaixo":

```js
// t de 0 (início do degradê) a 1 (borda); alpha = maxA * smoothstep(t)^1.15
const ease = t => { const s = t*t*(3-2*t); return Math.pow(s, 1.15); };
// maxA ≈ 0,90 na borda; o degradê começa uns 12% antes de onde o texto começa
```

- A metade do degradê fica abaixo de 50% de opacidade, para a foto aparecer. Só a borda chega
  perto de 90%, para garantir a leitura do texto e esconder artefatos.
- **Fade branco do BANNER-SITE**: transparente em 60% da altura, depois 0,12 (66%), 0,40 (71%),
  0,75 (76%), 0,95 (81%) e 1,0 a partir de 85%.

---

## 7. Stories animado (vídeo)

O Figma anima camadas, mas **não é editor de vídeo**. Ele aceita vídeo de no máximo ~100MB e a
IA só envia imagens de até 10MB. O fluxo aprovado é **Figma para a arte + ffmpeg para o vídeo**:

1. **Camadas**: duplicar o STORIES 3 vezes, sem foto e sem fundo (`fills = []`):
   gradientes / topo (logo + tag + título) / base (só o subtítulo; **botão oculto**). Exportar com
   `get_screenshot` (`maxDimension: 1920`, `contentsOnly: true`). Sai PNG RGBA transparente:
   `ov_grad.png`, `ov_top.png`, `ov_bot.png`.
2. **Vídeo**: o usuário manda um link do Google Drive. Para baixar:
   `curl -L -o src.mp4 "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t"`.
   O case Giadamarina tinha ~900MB, 4K e 25fps.
3. **Escolher cenas**: extrair 1 quadro a cada 2s (`ffmpeg -vf fps=1/2`), montar folha de contato
   com timestamps e escolher **produto → produção → tecnologia Audaces** (fechar na máquina com a
   logo Audaces). **Evitar** cenas com rosto no terço superior (ficam sob o título) e cenas com
   legenda gravada. Gerar prévia 9:16 com as camadas por cima antes de renderizar.
4. **Música**: sem áudio original, só a trilha enviada. Medir o BPM (autocorrelação do onset) e
   começar num tempo forte de um trecho com energia. Giadamarina: "Kiara" (Bonobo), ≈129 bpm,
   início em 59,675s.
5. **Cortes**: cada cena = **4 batidas** (≈1,86s), o que dá **8 cenas ≈ 15s** (16 cenas ≈ 30s).
6. **Textos visíveis desde o início** (fade de 0,7s no primeiro segundo) e **sem o botão
   "SCOPRI LA STORIA" no vídeo**. O usuário pediu isso explicitamente. Oculte o botão na camada
   "base" e reancore o subtítulo na margem de 250px (`y = 1920 − 250 − altura do bloco`).
7. **Saída**: MP4 H.264 1080×1920, 25fps, CRF 18, AAC 192k, `+faststart` (≈12MB para 15s).
   Enviar ao usuário com `SendUserFile`. **Não** commitar vídeos no repositório.

Script: [`scripts/render.py`](scripts/render.py), com o exemplo de cenas em
[`scripts/shots.txt`](scripts/shots.txt) (formato: `segundo_inicial centro_x_0a1`).

```bash
python3 scripts/render.py
```

O comando roda na pasta com `src.mp4`, `music.mp3`, `shots.txt` e os 3 PNGs. `BEAT`,
`MUSIC_START` e `OUT` ficam no topo do script.

---

## 8. Pegadinhas técnicas (Figma Plugin API / MCP)

- Seletores do `node.query()` **falham com acentos** (`Título`, `Subtítulo`, `símbolo`). Use
  `findAll(n => n.name === 'Título')`.
- **Margem e centralização**: depois de mudar a fonte ou o texto, recalcule `y` do bloco
  (`y = alturaFrame − margem − bloco.height`). O auto-layout em HUG muda de altura.
- **Trocar a logo**: clonar `13:40`, `rescale(tamanho / largura)`, inserir no frame do formato
  (fora do auto-layout) e posicionar em x/y absolutos.
- `instance.rescale()` cria override de `cornerRadius`; ajuste o raio depois de escalar.
- Reenquadrar foto: alterar `imageTransform` do fill (`scaleMode: CROP`), por exemplo
  `[[sx,0,tx],[0,sy,ty]]`. Mantenha `sx/sy` na proporção do frame.
- Sempre `await figma.loadFontAsync({family:'Sora', style:'Bold'})` / `({family:'Poppins', style:'Medium'})`
  antes de editar texto. Atenção: no Inter o peso é `"Semi Bold"` (com espaço), em Sora/Poppins é `"SemiBold"`.
- Verificação visual: screenshot do frame `8:11` inteiro (`maxDimension` 2048+) e de cada
  formato ao lado da referência correspondente.

---

## 9. Checklist final (conferir formato a formato)

- [ ] Logo **oficial**, no tamanho e posição da tabela da seção 5 (nenhuma no LinkedIn, banner e miniatura)
- [ ] Título "Audaces + Cliente" (com **+**), sem placeholders em lugar nenhum
- [ ] Fontes **Sora** (título) e **Poppins** (demais textos), sem Inter
- [ ] Stories em vídeo **sem botão**
- [ ] Margens: 80px; Stories 250px em cima e embaixo
- [ ] Blocos com **largura fixa** e centro do bloco = centro do frame (ou alinhamento correto no e-mail e no LinkedIn)
- [ ] Botão com raio ≈ 1/3 da altura
- [ ] Degradê suave; nenhuma faixa preta dura; foto visível
- [ ] Nenhum texto sobre o rosto
- [ ] Bordas da foto sem legenda ou artefato de vídeo
- [ ] BANNER-SITE: foto + fade branco, pessoa inteira acima do fade
- [ ] MINIATURA-LP: só a foto
- [ ] Screenshot final enviado ao usuário, com a lista do que foi decidido por julgamento
