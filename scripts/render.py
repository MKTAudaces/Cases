"""
Monta um Stories animado (1080x1920) a partir de um vídeo horizontal + camadas do Figma + música.

Uso (na pasta onde estão os arquivos):
    python3 render.py

Arquivos esperados na pasta atual:
    src.mp4       vídeo original (16:9, qualquer resolução)
    music.mp3     trilha
    shots.txt     lista de cenas: "<segundo_inicial> <centro_x_0a1>" por linha
    ov_grad.png   camada de degradês (PNG transparente 1080x1920 exportado do Figma)
    ov_top.png    camada logo + tag + título
    ov_bot.png    camada subtítulo + botão

Requer ffmpeg instalado.
"""
import json
import subprocess

# ---------------- CONFIGURAÇÃO ----------------
BEAT = 0.46439909      # duração de 1 batida da música em segundos (Kiara/Bonobo ≈ 129 bpm)
BEATS_PER_SHOT = 4     # cada cena dura 4 batidas (≈1,86s)
MUSIC_START = 59.675   # segundo da música onde o vídeo começa (escolher um tempo forte)
OUT = "story_15s.mp4"
OUT_W, OUT_H, FPS = 1080, 1920, 25
# ----------------------------------------------


def probe_size(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height", "-of", "json", path],
        capture_output=True, text=True, check=True).stdout
    s = json.loads(out)["streams"][0]
    return s["width"], s["height"]


def main():
    src_w, src_h = probe_size("src.mp4")
    crop_w = round(src_h * OUT_W / OUT_H)  # largura do recorte vertical 9:16 dentro do quadro 16:9
    D = BEATS_PER_SHOT * BEAT
    shots = [tuple(map(float, l.split())) for l in open("shots.txt") if l.strip()]
    N = len(shots)
    T = N * D

    args = ["ffmpeg", "-v", "error", "-y"]
    for t, _ in shots:
        args += ["-ss", f"{t:.3f}", "-t", f"{D:.4f}", "-i", "src.mp4"]
    for layer in ("ov_grad.png", "ov_top.png", "ov_bot.png"):
        args += ["-loop", "1", "-t", f"{T:.3f}", "-i", layer]
    args += ["-ss", f"{MUSIC_START}", "-t", f"{T:.3f}", "-i", "music.mp3"]

    f = []
    for i, (_, cx) in enumerate(shots):
        x = int(max(0, min(src_w - crop_w, cx * src_w - crop_w / 2)))
        f.append(f"[{i}:v]crop={crop_w}:{src_h}:{x}:0,scale={OUT_W}:{OUT_H}:flags=lanczos,"
                 f"fps={FPS},setsar=1,trim=duration={D:.4f},setpts=PTS-STARTPTS[v{i}]")
    f.append("".join(f"[v{i}]" for i in range(N)) +
             f"concat=n={N}:v=1:a=0,format=yuv420p,fade=t=in:st=0:d=0.3[base]")
    f.append(f"[{N}:v]format=rgba[g]")
    # textos e botão aparecem desde o início, com fade de 0,7s
    f.append(f"[{N+1}:v]format=rgba,fade=t=in:st=0.3:d=0.7:alpha=1[tp]")
    f.append(f"[{N+2}:v]format=rgba,fade=t=in:st=0.3:d=0.7:alpha=1[bt]")
    f.append("[base][g]overlay=shortest=1[a1];[a1][tp]overlay=shortest=1[a2];"
             "[a2][bt]overlay=shortest=1,format=yuv420p[vout]")
    f.append(f"[{N+3}:a]afade=t=in:st=0:d=0.3,afade=t=out:st={T-1.5:.3f}:d=1.5[aout]")

    args += ["-filter_complex", ";".join(f), "-map", "[vout]", "-map", "[aout]",
             "-t", f"{T:.3f}", "-c:v", "libx264", "-preset", "slow", "-crf", "18",
             "-profile:v", "high", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
             "-movflags", "+faststart", OUT]
    subprocess.run(args, check=True, stdin=subprocess.DEVNULL)
    print(f"OK: {OUT} ({T:.2f}s, {N} cenas)")


if __name__ == "__main__":
    main()
