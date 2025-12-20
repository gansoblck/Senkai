import os
from PIL import Image

class image:

    def __init__(self, caminho_origem, corte_altura, corte_largura, pasta_destino) -> None:
        self.caminho_origem = caminho_origem
        self.corte_altura = corte_altura
        self.corte_largura = corte_largura
        self.pasta_destino = pasta_destino

    def crop_images(self):
        if not os.path.exists(self.caminho_origem):
            return "Pasta de origem não encontrada"
        
        if not os.path.exists(self.pasta_destino):
            os.makedirs(self.pasta_destino)

        for arquivo in os.listdir(self.caminho_origem):
            if arquivo.endswith(('.png', '.jpeg', '.jpg')):
                caminho_imagem: str = os.path.join(self.caminho_origem, arquivo)
                imagem = Image.open(caminho_imagem)
                largura, altura = imagem.size

                altura_corte: int = int(altura * (1 - self.corte_altura))
                largura_corte: int = int(altura * (1 - self.corte_largura))
                caixa_corte = (0, 0, largura_corte, altura_corte)

                imagem_cortada = imagem.crop(caixa_corte)
                caminho_salvar = os.path.join(self.pasta_destino, f"cortada_{arquivo}")
                imagem_cortada.save(caminho_salvar)

        return f"Imagens cortadas e salvas em {self.pasta_destino}"
