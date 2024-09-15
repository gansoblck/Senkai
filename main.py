import os
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from PIL import Image

def selecionar_pasta_origem():
    pasta_origem = filedialog.askdirectory(title="Selecione a pasta com as imagens")
    entrada_pasta_origem.delete(0, 'end')
    entrada_pasta_origem.insert(0, pasta_origem)

def selecionar_pasta_saida():
    pasta_saida = filedialog.askdirectory(title="Selecione a pasta para salvar as imagens cortadas")
    entrada_pasta_saida.delete(0, 'end')
    entrada_pasta_saida.insert(0, pasta_saida)

def cortar_imagens():
    pasta_imagens = entrada_pasta_origem.get()
    pasta_saida = entrada_pasta_saida.get()
    
    try:
        porcentagem_corte_altura = float(entrada_altura.get()) / 100
        porcentagem_corte_largura = float(entrada_largura.get()) / 100
    except ValueError:
        messagebox.showerror("Erro", "Insira valores numéricos válidos para o corte!")
        return

    if not os.path.exists(pasta_imagens):
        messagebox.showerror("Erro", "Pasta de origem não encontrada!")
        return
    
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)
    
    total_imagens = len([f for f in os.listdir(pasta_imagens) if f.endswith(('.png', '.jpg', '.jpeg'))])
    if total_imagens == 0:
        messagebox.showerror("Erro", "Nenhuma imagem encontrada na pasta de origem!")
        return

    contador = 0
    for arquivo in os.listdir(pasta_imagens):
        if arquivo.endswith(('.png', '.jpg', '.jpeg')):
            try:
                caminho_imagem = os.path.join(pasta_imagens, arquivo)
                imagem = Image.open(caminho_imagem)
                largura, altura = imagem.size

                nova_altura = int(altura * (1 - porcentagem_corte_altura))
                nova_largura = int(largura * (1 - porcentagem_corte_largura))
                caixa_corte = (0, 0, nova_largura, nova_altura)

                imagem_cortada = imagem.crop(caixa_corte)
                caminho_salvar = os.path.join(pasta_saida, f"cortada_{arquivo}")
                imagem_cortada.save(caminho_salvar)

                contador += 1
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao processar {arquivo}: {e}")
                return

    messagebox.showinfo("Sucesso", f"{contador} imagens cortadas e salvas na pasta '{pasta_saida}'.")

# Criando a interface gráfica
app = Tk()
app.title("Cortar Imagens em Massa")
app.geometry("500x300")

# Labels e Campos de Entrada
Label(app, text="Pasta de origem:").pack(pady=5)
entrada_pasta_origem = Entry(app, width=50)
entrada_pasta_origem.pack(pady=5)
Button(app, text="Selecionar Pasta", command=selecionar_pasta_origem).pack(pady=5)

Label(app, text="Pasta de saída:").pack(pady=5)
entrada_pasta_saida = Entry(app, width=50)
entrada_pasta_saida.pack(pady=5)
Button(app, text="Selecionar Pasta", command=selecionar_pasta_saida).pack(pady=5)

Label(app, text="Corte de Altura (%):").pack(pady=5)
entrada_altura = Entry(app, width=10)
entrada_altura.pack(pady=5)

Label(app, text="Corte de Largura (%):").pack(pady=5)
entrada_largura = Entry(app, width=10)
entrada_largura.pack(pady=5)

Button(app, text="Cortar Imagens", command=cortar_imagens).pack(pady=20)

# Iniciar a aplicação
app.mainloop()
