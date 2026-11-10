# Repositório Cases (Marketing Audaces)

Este repositório guarda o padrão das artes dos **Cases de Sucesso Audaces**.

## Regra principal

Antes de qualquer trabalho de arte, copy ou vídeo de case, **leia
[`GUIA-ARTES-CASES.md`](GUIA-ARTES-CASES.md) inteiro** e siga-o. Ele registra os erros já
cometidos e as especificações aprovadas (fontes Sora + Poppins, margens, tamanhos de logo
por formato, botão, degradê, idiomas, nomes de arquivo, foto redonda, Stories em vídeo).

## Fluxo de um case novo

### 1. Conferir se o pedido está completo

Para começar, o pedido precisa ter:

1. **Link do arquivo do Figma do case**, com a(s) **foto(s) já colada(s) na página**.
2. **Copy** (blocos LP / TYP / ADS). Dela se tira **a frente/idioma**: Itália (IT), Brasil (PT-BR),
   LATAM (ES-LATAM) ou Global (EN-Global), e o **nome da empresa cliente**.

Se faltar a foto ou a copy, **não comece**: peça o que falta, de forma curta e objetiva. Exemplo:
"Para criar o case preciso da copy e da foto colada na página do Figma. Pode me mandar?". Se a frente
não estiver clara pela copy, pergunte também. Vídeo e música só são necessários se pedirem o Stories
animado ou o GIF.

**Se o pedido vier sem nada** (ex.: "preciso criar uma arte nova de case"), responda com este passo a
passo, adaptando só o necessário:

> Para criar o case, preciso de 3 coisas:
> 1. **Arquivo no Figma**: crie um arquivo novo (pode ser vazio), cole nele a(s) foto(s) do case e me
>    mande o link. Os formatos eu puxo do template oficial.
> 2. **Copy do case** (blocos LP / TYP / ADS).
> 3. **Frente**: Itália, Brasil, LATAM ou Global (inglês), se não estiver clara na copy.
>
> Se também quiser o **Stories animado** ou o **GIF**, mande o link do vídeo (Google Drive com acesso
> "qualquer pessoa com o link") e a música.

Não peça nada além disso (o template, as fontes e as regras já estão no guia).

### 2. Montar as artes

1. **Template oficial**: página **"Template — Cases de Sucesso"** do arquivo "Referências e Padrões"
   (seção 3 do guia, com as chaves). Importe os formatos com `figma.importComponentByKeyAsync(key)` no
   arquivo do case. Se a importação falhar, a biblioteca não está publicada ou ativada: peça ao usuário
   para publicar/ativar (Assets → Libraries) antes de continuar. A Plugin API **não copia nós entre
   arquivos**, então nunca reconstrua os formatos do zero sem avisar.
2. **Foto**: a foto colada na página já tem `imageHash`. Leia esse hash no fill do nó da foto e aplique
   na camada `Foto (substituir)` de cada instância:
   `foto.fills=[{type:'IMAGE',imageHash,scaleMode:'CROP',imageTransform:[[sx,0,tx],[0,sy,ty]]}]`.
   Enquadre por formato: rosto livre de texto, sem legenda gravada nas bordas.
   Se a foto vier pelo chat (arquivo local, PNG/JPG, **máx. 10MB**), use `upload_assets` **sem**
   `nodeIds` (ele não aceita IDs de camadas de instância, ex. `I2:23;19:7`), pegue o `imageHash` da
   resposta e apague o nó temporário (`placedOnNodeId`).
3. **Copy e idioma**: título "Audaces +" / "Empresa"; subtítulo = bloco ADS no idioma da frente;
   variante `Idioma` da tag e do botão (seção 4 do guia).
4. **Foto redonda do usuário**: se houver uma pessoa na foto/vídeo do case, gere também o componente
   `Foto redonda / Usuário` (300×300, seção 3 do guia), com o rosto centralizado.
5. **Nomes**: renomeie cada instância no padrão
   `Case_Empresa_FORMATO_LARGURAxALTURA-PROPORÇÃO_FRENTE` (seção 4.1 do guia), porque a exportação do
   Figma usa o nome da camada.
6. Confira cada formato pelo checklist da seção 9 do guia e entregue com screenshot.

## Vídeo (Stories animado) e GIF

Só se pedirem. Siga a seção 7 do guia e use `scripts/render.py`. As camadas do vídeo são exportadas no
**idioma da frente** (variante `Idioma`), com o subtítulo da copy daquela frente. Vídeos e músicas
**não** são commitados. Entregue os arquivos pelo chat, com o mesmo padrão de nome.

## Idioma

Responda ao usuário em **português**.
