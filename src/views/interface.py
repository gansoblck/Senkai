from tkinter import filedialog, StringVar, DoubleVar
import ttkbootstrap as ttk 
from models.image import image

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

images = image(caminho_origem= str(origem), corte_altura=corte_h, corte_largura=corte_w, pasta_destino= str(destino))
resultado = images.crop_images

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

ttk.Button(app, text="Cortar Imagens", command=images.crop_images, bootstyle="success").pack(pady=20)
ttk.Label(app, textvariable=resultado, bootstyle="info").pack(pady=5)


def main():
    app.mainloop()


if __name__ == "__main__":
    app.mainloop()
