# Repositório Cases (Marketing Audaces)

Este repositório guarda o padrão das artes dos **Cases de Sucesso Audaces**.

## Regra principal

Antes de qualquer trabalho de arte, copy ou vídeo de case, **leia
[`GUIA-ARTES-CASES.md`](GUIA-ARTES-CASES.md) inteiro** e siga-o. Ele registra os erros já
cometidos e as especificações aprovadas (fontes Sora + Poppins, margens, tamanhos de logo
por formato, botão, degradê, padrões de banner/miniatura/LinkedIn/e-mail, Stories em vídeo).

## Ao receber um novo case (copy + fotos + link do Figma)

1. **Template oficial**: página **"Template — Cases de Sucesso"** do arquivo "Referências e
   Padrões" (seção 3 do guia, com as chaves dos componentes). Importe os componentes de formato
   com `figma.importComponentByKeyAsync(key)` no arquivo do case que o usuário mandar e preencha
   as propriedades `Título` e `Subtítulo`. Se a importação falhar, a biblioteca não está publicada
   ou ativada: peça ao usuário para publicar/ativar (Assets → Libraries) antes de continuar. A Plugin
   API **não copia nós entre arquivos**, então nunca reconstrua os formatos do zero sem avisar.
2. **Fotos enviadas no chat**: chegam como arquivos locais. Para colocá-las no Figma use
   `upload_assets` com `nodeIds` = os retângulos `Foto` de cada formato (PNG/JPG, **máx. 10MB**;
   comprima com Pillow se precisar). Depois ajuste o enquadramento por formato: rosto livre de
   texto, nada de legenda gravada nas bordas.
3. **Copy**: use o bloco ADS da copy, adaptado conforme a seção 4 do guia ("Audaces + Cliente").
4. Confira cada formato pelo checklist da seção 9 do guia antes de entregar, com screenshot.

## Vídeo (Stories animado)

Siga a seção 7 do guia e use `scripts/render.py`. Vídeos e músicas **não** são commitados.
Entregue o MP4 ao usuário pelo chat.

## Idioma

Responda ao usuário em **português**.
