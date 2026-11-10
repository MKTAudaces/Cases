# Guia de artes para Cases de Sucesso Audaces

> **Para a IA que vai executar o próximo case: leia este arquivo inteiro antes de qualquer
> chamada ao Figma.** Ele foi escrito depois do case **Giadamarina** (nov/2026), em que a
> primeira entrega veio com vários erros: logo errada, texto descentralizado, botão quadrado,
> degradê duro e formatos fora do padrão. Tudo o que foi corrigido está registrado aqui.
> Seguir este guia é obrigatório. Ele vale mais do que a sua intuição de design.

---

## 0. Fluxo obrigatório (resumo)

1. Ler este guia inteiro.
2. Abrir as **referências** (seção 2) e o **template oficial** (seção 3). Fazer screenshot
   dos formatos em tamanho real e **medir** (logo, tag, título, botão, margens) com
   [`scripts/medir_referencia.py`](scripts/medir_referencia.py). Não estime a olho.
3. **Usar o TEMPLATE OFICIAL** (seção 3): página **"Template — Cases de Sucesso"** no arquivo
   "Referências e Padrões". Os 8 formatos são **componentes** com as propriedades `Título` e
   `Subtítulo`. Não criar do zero, porque foi do zero que vieram os erros do início.
   - Se a biblioteca estiver publicada, importe os componentes no arquivo do case com
     `figma.importComponentByKeyAsync(key)` (chaves na seção 3) e crie instâncias. Funciona até
     em arquivo vazio.
   - Se a importação falhar (biblioteca não publicada ou não ativada), peça ao usuário para publicar
     ou ativar a biblioteca, ou para colar/duplicar a página do template no arquivo do case. A Plugin
     API **não copia nós entre arquivos**.
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

## 3. Template oficial (usar este)

Arquivo **Referências e Padrões** (fileKey `GyaCNTxVmORyOqJP1cwIxK`), página
**"Template — Cases de Sucesso"** (`21:14`). Link:
https://www.figma.com/design/GyaCNTxVmORyOqJP1cwIxK/Refer%C3%AAncias-e-Padr%C3%B5es

Seções da página:

| Seção | nodeId | Conteúdo |
|---|---|---|
| 00 · Leia-me | `22:142` | Como usar, regras fixas, padrões por formato, checklist |
| 01 · Fundamentos e componentes | `22:154` | Cores (variáveis), tipografia, logo, tag, botão |
| 02 · Formatos (componentes) | `22:178` | Os 9 componentes de formato, com foto provisória |
| 03 · Stories em vídeo — camadas | `22:179` | 3 instâncias do STORIES ANIMADO: gradientes / topo / base, para exportar como PNG transparente |
| 04 · Exemplo preenchido — Giadamarina | `22:180` | Instâncias preenchidas (foto + copy), como referência visual |

### Componentes (chaves para `importComponentByKeyAsync`)

| Componente | nodeId | key | Propriedades |
|---|---|---|---|
| Logo Audaces / Símbolo branco | `21:19` | `c56144597a5b83ba3892f4e0eb7dfea84d374ec2` | — (escalar com `rescale`) |
| Tag / Storia di successo (**component set**) | `25:148` | `603f0de04ffed9727d776f8bc5d42f8a09b19b26` | `Idioma` = IT · PT-BR · ES-LATAM · EN-Global |
| Botão CTA (**component set**) | `25:155` | `ee0e7c2373b011fa053512ced4aed8ce44a32e4d` | `Idioma` = IT · PT-BR · ES-LATAM · EN-Global |
| Foto redonda / Usuário (300×300) | `28:142` | `b0e61b800df698cb61a5e79a63fcca2ff83d7f5d` | camada `Foto (substituir)` |
| Formato / ADS 1080×1080 | `21:44` | `4a5859a113b7f72c287f07b414d8e3fd5634df8c` | `Título`, `Subtítulo` |
| Formato / FEED 1080×1350 | `21:45` | `b63827e463e4fbeeed3b339f55d91e797325f23c` | `Título`, `Subtítulo` |
| Formato / BANNER-SITE 1080×1350 | `21:46` | `2fa3b73e6a38d07b408d2b75bfc1ad60803f4677` | (texto oculto) |
| Formato / STORIES 1080×1920 | `21:47` | `eff26f7cf6a1cfb4706e31686c7396261735b008` | `Título`, `Subtítulo` |
| Formato / STORIES ANIMADO 1080×1920 | `21:48` | `a44bb2a026da0201c8fcb5bdde6e62dcfa85f8e3` | `Título`, `Subtítulo` (sem botão) |
| Formato / THUMBNAIL-YOUTUBE 1920×1080 | `21:49` | `e3b2609e800258a718a14a83afc0650cbd97996c` | `Título`, `Subtítulo` |
| Formato / CAPA-LINKEDIN 1920×1080 | `21:50` | `c01e20828ee273941d4975ddd0eb767853e24cc4` | `Título` |
| Formato / HEADER-E-MAIL 1200×600 | `21:51` | `40eeb6401cdbeb4980e6273cb7296b6206e35dc6` | `Título`, `Subtítulo` |
| Formato / MINIATURA-LP 1280×780 | `21:52` | `5362ce05fa373055efcd2f98625eff5c06d323c7` | (só foto) |

**Testado em 10/nov/2026** num arquivo vazio ("Teste Claudionho"): os 9 formatos foram importados da
biblioteca publicada, os textos foram preenchidos pelas propriedades e a foto foi trocada pelo método acima.

Variáveis de cor (coleção **"Cases"**): `cta/laranja` #FF5E00 (fill do botão), `texto/branco`
#FFFFFF (textos e contorno da tag), `overlay/base` #0A0A0F (cor base dos degradês).

Os nomes das chaves de propriedade têm sufixo (ex.: `Título#21:0`). Leia
`instance.componentProperties` e procure pela que começa com `Título` / `Subtítulo`.

### Como montar um case novo a partir do template

```js
const ads = await figma.importComponentByKeyAsync("4a5859a113b7f72c287f07b414d8e3fd5634df8c");
const i = ads.createInstance();
const props = Object.keys(i.componentProperties);
i.setProperties({
  [props.find(p => p.startsWith("Título"))]: "Audaces +\nCliente",
  [props.find(p => p.startsWith("Subtítulo"))]: "Frase do bloco ADS\nem duas linhas.",
});
// Idioma da tag e do botão (instâncias expostas dentro do formato)
for (const n of i.findAll(n => n.type === "INSTANCE" && (n.name.startsWith("Tag") || n.name.startsWith("Botão"))))
  n.setProperties({ Idioma: "PT-BR" }); // IT | PT-BR | ES-LATAM | EN-Global
// Foto: upload_assets SEM nodeIds (ele não aceita IDs de camadas de instância, ex. "I2:23;19:7"),
// POST do arquivo → resposta traz imageHash e placedOnNodeId (nó temporário). Depois:
const foto = i.findOne(n => n.name === "Foto (substituir)");
foto.fills = [{ type: "IMAGE", imageHash: HASH, scaleMode: "CROP",
                imageTransform: [[sx, 0, tx], [0, sy, ty]] }]; // enquadrar: rosto livre de texto
(await figma.getNodeByIdAsync(PLACED_ON_NODE_ID)).remove();
```

Camadas de cada formato: `Foto (substituir)` (fill de imagem, `scaleMode: CROP`), `Gradiente`
(1 ou 2 retângulos), `Logo Audaces` (instância), `Conteúdo` (auto-layout vertical: tag, `Título`,
`Subtítulo`, botão).

- **Textos muito longos** (nome de cliente comprido): reduza o tamanho do título na instância
  até caber com a margem de 80px e mantenha a centralização. Avise o usuário.
- **Ao mudar o template**: edite o componente principal, peça ao usuário para **publicar** a
  biblioteca de novo e atualize este guia.

### Case Giadamarina (arquivo original)

fileKey `ajnYMWhZIiZEmOnUxxqoeM`, frame `8:11`. É o case que deu origem ao template. Só use para
consulta: o template acima é a fonte oficial.

---

## 4. Copy: como adaptar

- **Primeiro identifique a frente (mercado/idioma) do case**: Itália, Brasil, LATAM ou Global (inglês).
  Se a copy não deixar claro, pergunte. Um case pode sair em mais de uma frente: monte um conjunto
  de formatos por idioma (ex.: uma página do Figma por idioma).
- A copy chega em blocos LP / TYP / ADS. **As artes usam o bloco ADS**:
  - título: **"Audaces +" / "Cliente"** em 2 linhas, Title Case, igual em todos os idiomas. Nunca usar "x" e nunca caixa alta, mesmo que a copy venha assim;
  - subtítulo: a frase do ADS **no idioma da frente**, quebrada em 2 linhas equilibradas (ex.: "La tradizione Made in Italy evolve / con l'automazione.");
  - tag e botão: escolha a variante **`Idioma`** na tag e no botão de cada formato (`instancia.setProperties({Idioma: "PT-BR"})`).

| Frente | `Idioma` | Tag | Botão |
|---|---|---|---|
| Itália | `IT` | STORIA DI SUCCESSO | SCOPRI LA STORIA |
| Brasil | `PT-BR` | CASE DE SUCESSO | ASSISTA AGORA |
| LATAM (espanhol) | `ES-LATAM` | CASO DE ÉXITO | VER LA HISTORIA |
| Global (inglês) | `EN-Global` | SUCCESS STORY | WATCH THE STORY |

- Os CTAs acima são para **destino em vídeo** (o padrão dos cases). Se o destino for texto, ajuste
  o botão (EN: *Read the story*; regra do manual de marca). PT-BR vem do case Univali; ES-LATAM e
  EN seguem o glossário da skill `formato-traducao-ingles` / `marca-audaces`. Valide com o time
  antes da primeira publicação em cada frente.
- **Inglês**: siga a skill `formato-traducao-ingles`. **Espanhol/português**: `marca-audaces` → idiomas.
  Nomes de produto mudam por mercado (ex.: Audaces Encaixe = Audaces Tizada em espanhol,
  Audaces Marker em inglês/italiano).
- "Não precisa seguir à risca": priorize a consistência com as outras artes do case.
- LP, TYP, título SEO e meta description **não fazem parte das artes**. Só crie telas de LP
  se o usuário pedir explicitamente.

### 4.1 Nome dos arquivos exportados

Padrão: **`Case_Empresa_FORMATO_LARGURAxALTURA-PROPORÇÃO_FRENTE`**

- **Empresa**: nome do cliente sem espaços nem acentos (ex.: `Giadamarina`, `ModaMagia`).
- **FORMATO** e **resolução**:

| Formato | Resolução-proporção |
|---|---|
| `ADS` | `1080x1080-1x1` |
| `FEED` | `1080x1350-4x5` |
| `BANNER-SITE` | `1080x1350-4x5` |
| `STORIES` | `1080x1920-9x16` |
| `STORIES-ANIMADO` (MP4) | `1080x1920-9x16` |
| `THUMBNAIL-YOUTUBE` | `1920x1080-16x9` |
| `CAPA-LINKEDIN` | `1920x1080-16x9` |
| `HEADER-EMAIL` | `1200x600-2x1` |
| `MINIATURA-LP` | `1280x780-64x39` |
| `FOTO-REDONDA` | `300x300-1x1` |
| `VIDEO-FUNDO` (MP4) | `1920x1080-16x9` |
| `GIF` | `600x338-16x9` (tamanho real do GIF) |

- **FRENTE**: `IT`, `PT-BR`, `ES-LATAM` ou `EN-Global`.
- A proporção usa `x` (`1x1`) porque `/` e `:` não são permitidos em nome de arquivo.
- Exemplos: `Case_Giadamarina_ADS_1080x1080-1x1_IT.png` · `Case_Giadamarina_STORIES-ANIMADO_1080x1920-9x16_PT-BR.mp4`.
- No Figma, **renomeie cada instância com esse nome** (sem extensão) e adicione export PNG 1x. Como a
  exportação usa o nome da camada, "Export" já sai com o nome certo. Veja os exemplos na seção 04 do template.

### 4.2 Foto redonda do usuário (para LP e TYP)

As LPs e TYPs são feitas fora deste fluxo. Das artes, elas só precisam de **uma foto redonda da pessoa
que aparece no vídeo/foto do case** (quando houver pessoa).

- Use o componente **`Foto redonda / Usuário`** (300×300, círculo, sem borda).
- Enquadramento: rosto centralizado, olhos a ~40% da altura, ombros visíveis (como no exemplo
  `Case_Giadamarina_FOTO-REDONDA_300x300-1x1_IT` da seção 04 do template).
- Troque o fill da camada `Foto (substituir)` (`scaleMode: CROP` + `imageTransform`).
- Exporte PNG transparente 1x e 2x (`@2x`), com o padrão de nome da seção 4.1.

---

## 5. Especificação por formato

Regras gerais: margem **80px** (Stories: **250px** em cima e embaixo). Fontes oficiais dos cases: **Sora** (títulos) e **Poppins** (demais textos). Ver seção 5.1.

| Formato | Logo | Layout | Textos (px) |
|---|---|---|---|
| **ADS 1080×1080** | 50, centralizado, topo y=80 | Bloco centralizado, largura fixa 864 (x=108), **na base**, terminando em y=1000 | Tag h49 · Título 84 · Subtítulo 30 · Botão h66 (raio 22) · gap 24 |
| **FEED 1080×1350** | 50, centralizado, topo y=80 | Igual ao ADS, terminando em y=1270 | Igual ao ADS |
| **STORIES 1080×1920** | 79, centralizado, topo y=250 | Topo: tag + título, largura 864, início y≈413, gap 36. Base: subtítulo + botão, largura 864, gap 44, terminando em y=1670 | Tag h67 · Título 112 · Subtítulo 36 · Botão h79 (raio 26) |
| **THUMBNAIL-YOUTUBE 1920×1080** | 58, centralizado sobre o bloco, 70px acima da tag | Coluna largura 760, **texto centralizado**, no lado oposto ao da pessoa (Giadamarina: x=1025), centralizada na vertical | Tag h49 · Título 100 · Subtítulo 34 · **sem botão** · gap 32 |
| **CAPA-LINKEDIN 1920×1080** | **nenhuma** | Tag + título **alinhados à esquerda**, lado oposto ao da pessoa (x=1030), centralizados na vertical, gap 40 | Tag h65 · Título 120 (com Sora, 128 estoura a margem) · **sem subtítulo e sem botão** |
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
| **Tag** | Variante `Idioma` (seção 4). Pílula (raio 999), contorno branco 2px, sem preenchimento, Poppins **Medium 22**, maiúsculas, espaçamento 6%, padding 26×11 → ≈292×49 |
| **Botão** | Variante `Idioma` (seção 4). Preenchimento laranja `#FF5E00` (referência mede `#FF6700`), Poppins **SemiBold 28** branco, espaçamento 2%, padding 36×16 → ≈342×66, **raio 22** |
| **Título** | **Sora Bold**, entrelinha 95%, espaçamento −2%, branco |
| **Subtítulo** | **Poppins Medium**, entrelinha 130%, branco |

### 5.1 Fontes

- **Fontes oficiais dos cases: Sora e Poppins** (definição do time de marketing). Não use Inter.
- Divisão adotada: **Sora** no título ("Audaces + Cliente"); **Poppins** no subtítulo, na tag e
  no botão. Os pesos estão na tabela de componentes acima.
- Nomes exatos no Figma (sem espaço): Sora `Bold`/`SemiBold`/`ExtraBold`; Poppins `Medium`/`SemiBold`/`Bold`.
  Sempre `await figma.loadFontAsync(...)` antes de editar.
- O template oficial (seção 3) já está em Sora + Poppins.
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
7. **Uma versão por frente**: se o case sai em mais de um idioma, troque a variante `Idioma` (tag; o
   Stories em vídeo não tem botão) e o subtítulo para a copy daquela frente nas camadas, reexporte os PNGs
   e renderize de novo. Os cortes e a música podem ser os mesmos, salvo pedido diferente.
8. **GIF / vídeo de fundo** (ex.: para RD Station): mesmos cortes, quadro inteiro 16:9, sem textos e sem
   música. O GIF fica com 600px de largura e ~17fps (≈5–6MB para 15s). Em 1920px ele passa de 40MB.
   Use `hqdn3d` + `palettegen`/`paletteuse` (ffmpeg) + `gifsicle -O3 --lossy=200`.
9. **Saída**: MP4 H.264 1080×1920, 25fps, CRF 18, AAC 192k, `+faststart` (≈12MB para 15s).
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
- **Logo**: use sempre uma instância do componente `Logo Audaces / Símbolo branco` (key na seção 3),
  `rescale(tamanho / largura)`, fora do auto-layout, em x/y absolutos.
- **Nunca use `rescale()` no componente principal que já tem instâncias**: as instâncias encolhem
  junto e o conteúdo fica minúsculo. Se precisar, corrija com `resetOverrides()` nas instâncias.
- **Tamanho e posição de filhos de instância não podem ser alterados.** Se um texto mais longo fizer
  o bloco passar da margem (ex.: subtítulo em 3 linhas), use `instance.detachInstance()` e reposicione
  o bloco (`y = alturaFrame − margem − bloco.height`).
- `instance.rescale()` cria override de `cornerRadius`; ajuste o raio depois de escalar.
- Reenquadrar foto: alterar `imageTransform` do fill (`scaleMode: CROP`), por exemplo
  `[[sx,0,tx],[0,sy,ty]]`. Mantenha `sx/sy` na proporção do frame.
- Sempre `await figma.loadFontAsync({family:'Sora', style:'Bold'})` / `({family:'Poppins', style:'Medium'})`
  antes de editar texto. Atenção: no Inter o peso é `"Semi Bold"` (com espaço), em Sora/Poppins é `"SemiBold"`.
- Verificação visual: screenshot de todos os formatos do case (`maxDimension` 2048+) e de cada
  formato ao lado da instância de exemplo correspondente (seção 04 do template).

---

## 9. Checklist final (conferir formato a formato)

- [ ] Logo **oficial**, no tamanho e posição da tabela da seção 5 (nenhuma no LinkedIn, banner e miniatura)
- [ ] Título "Audaces + Cliente" (com **+**), sem placeholders em lugar nenhum
- [ ] Tag e botão na variante `Idioma` da frente do case; subtítulo no mesmo idioma
- [ ] Instâncias renomeadas no padrão `Case_Empresa_FORMATO_RESOLUÇÃO_FRENTE`
- [ ] Foto redonda do usuário gerada (se houver pessoa no case)
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
