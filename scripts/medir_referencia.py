"""
Mede elementos em referências achatadas (PNG exportado do Figma em tamanho real, escala 1x).

As referências do arquivo "Referências e Padrões" são IMAGENS, não camadas. Por isso os
tamanhos têm que ser medidos em pixels. Exporte cada formato com get_screenshot usando
maxDimension = maior lado real do frame (ex.: 1920) e rode:

    python3 medir_referencia.py ref.png                          # botão laranja (posição, tamanho, raio)
    python3 medir_referencia.py ref.png --branco X0 Y0 X1 Y1     # caixa de pixels brancos numa região
                                                                 # (logo, tag, título, subtítulo)
"""
import argparse

import numpy as np
from PIL import Image


def botao(im):
    r, g, b = im[..., 0], im[..., 1], im[..., 2]
    m = (r > 220) & (g > 70) & (g < 140) & (b < 60)  # laranja Audaces
    rows, cols = m.sum(1), m.sum(0)
    yr, xr = np.nonzero(rows > 20)[0], np.nonzero(cols > 5)[0]
    if len(yr) == 0:
        print("Nenhum botão laranja encontrado.")
        return
    y0, y1, x0, x1 = yr.min(), yr.max(), xr.min(), xr.max()
    h, w = y1 - y0 + 1, x1 - x0 + 1
    # raio ≈ quantas linhas a borda esquerda leva até ficar reta
    prof = [int(np.argmax(m[y, x0:x0 + 80])) for y in range(y0, y0 + h // 2)]
    raio = next((i for i, v in enumerate(prof) if v == 0), h // 2)
    cor = im[(y0 + y1) // 2, x0 + 4]
    print(f"Botão: x={x0} y={y0} w={w} h={h} centro_x={(x0 + x1) / 2:.0f} "
          f"raio≈{raio}px ({raio / h:.2f}×altura) cor=#{cor[0]:02X}{cor[1]:02X}{cor[2]:02X} "
          f"margem_inferior={im.shape[0] - y1 - 1}")


def branco(im, box, thr=228):
    x0, y0, x1, y1 = box
    m = im[y0:y1, x0:x1].min(-1) > thr
    ys, xs = np.nonzero(m)
    if len(xs) == 0:
        print("Nenhum pixel branco na região.")
        return
    bx, by = x0 + xs.min(), y0 + ys.min()
    w, h = xs.max() - xs.min() + 1, ys.max() - ys.min() + 1
    print(f"Branco: x={bx} y={by} w={w} h={h} centro_x={bx + w / 2:.0f} "
          f"(largura da imagem {im.shape[1]}, centro {im.shape[1] / 2:.0f})")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("imagem")
    ap.add_argument("--branco", nargs=4, type=int, metavar=("X0", "Y0", "X1", "Y1"))
    a = ap.parse_args()
    img = np.array(Image.open(a.imagem).convert("RGB")).astype(int)
    if a.branco:
        branco(img, a.branco)
    else:
        botao(img)
