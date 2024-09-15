import os
from tkinter import filedialog, StringVar, DoubleVar
from PIL import Image
import ttkbootstrap as ttk  # Certifique-se de usar ttkbootstrap

def cortar_imagens():
    pasta_origem = origem.get()
    pasta_destino = destino.get()
    corte_altura = corte_h.get()
    corte_largura = corte_w.get()

    if not os.path.exists(pasta_origem):
        resultado.set("Pasta de origem não encontrada!")
        return

    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    for arquivo in os.listdir(pasta_origem):
        if arquivo.endswith(('.png', '.jpg', '.jpeg')):
            caminho_imagem = os.path.join(pasta_origem, arquivo)
            imagem = Image.open(caminho_imagem)
            largura, altura = imagem.size

            altura_corte = int(altura * (1 - corte_altura))
            largura_corte = int(largura * (1 - corte_largura))
            caixa_corte = (0, 0, largura_corte, altura_corte)

            imagem_cortada = imagem.crop(caixa_corte)
            caminho_salvar = os.path.join(pasta_destino, f"cortada_{arquivo}")
            imagem_cortada.save(caminho_salvar)

    resultado.set(f"Imagens cortadas e salvas em {pasta_destino}")

def escolher_pasta_origem():
    pasta = filedialog.askdirectory()
    origem.set(pasta)

def escolher_pasta_destino():
    pasta = filedialog.askdirectory()
    destino.set(pasta)

def atualizar_porcentagem_h(event):
    porcentagem_h.set(f"{corte_h.get() * 100:.0f}%")

def atualizar_porcentagem_w(event):
    porcentagem_w.set(f"{corte_w.get() * 100:.0f}%")

# Criando a janela principal
app = ttk.Window(themename="darkly")
app.title("Senkai - Batch Image Cropper")
app.geometry("600x600")

# Variáveis de controle
origem = StringVar()
destino = StringVar()
corte_h = DoubleVar(value=0.1)
corte_w = DoubleVar(value=0.1)
resultado = StringVar()
porcentagem_h = StringVar(value="10%")
porcentagem_w = StringVar(value="10%")

# Interface Gráfica
ttk.Label(app, text="Caminho da pasta de origem:", bootstyle="info").pack(pady=10)
ttk.Button(app, text="Selecionar Pasta", command=escolher_pasta_origem, bootstyle="primary").pack(pady=5)
ttk.Label(app, textvariable=origem).pack(pady=5)

ttk.Label(app, text="Caminho da pasta de destino:", bootstyle="info").pack(pady=10)
ttk.Button(app, text="Selecionar Pasta", command=escolher_pasta_destino, bootstyle="primary").pack(pady=5)
ttk.Label(app, textvariable=destino).pack(pady=5)

ttk.Label(app, text="Porcentagem de corte (altura):", bootstyle="info").pack(pady=10)
ttk.Scale(app, from_=0, to=1, orient="horizontal", variable=corte_h, command=atualizar_porcentagem_h, bootstyle="dark").pack(pady=5)
ttk.Label(app, textvariable=porcentagem_h, bootstyle="info").pack(pady=5)

ttk.Label(app, text="Porcentagem de corte (largura):", bootstyle="info").pack(pady=10)
ttk.Scale(app, from_=0, to=1, orient="horizontal", variable=corte_w, command=atualizar_porcentagem_w, bootstyle="dark").pack(pady=5)
ttk.Label(app, textvariable=porcentagem_w, bootstyle="info").pack(pady=5)

ttk.Button(app, text="Cortar Imagens", command=cortar_imagens, bootstyle="success").pack(pady=20)
ttk.Label(app, textvariable=resultado, bootstyle="info").pack(pady=5)

app.mainloop()
