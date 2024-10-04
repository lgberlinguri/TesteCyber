from PIL import Image
from torchvision import models, transforms
import torch
import torch.nn.functional as F

# Atualize os caminhos para as suas imagens na área de trabalho
image_path1 = "C:\\Users\\Usuario\\Desktop\\imagem1.png"
image_path2 = "C:\\Users\\Usuario\\Desktop\\imagem2.png"

# Carregar as imagens
image1 = Image.open(image_path1)
image2 = Image.open(image_path2)

# Definir a transformação a ser aplicada nas imagens
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Converter as imagens para RGB caso não estejam nesse formato
image1_rgb = image1.convert("RGB")
image2_rgb = image2.convert("RGB")

# Pré-processar as imagens
image1_tensor = preprocess(image1_rgb).unsqueeze(0)
image2_tensor = preprocess(image2_rgb).unsqueeze(0)

# Carregar o modelo pré-treinado ResNet50
model = models.resnet50(pretrained=True)
model.eval()

# Obter os vetores de características para ambas as imagens
with torch.no_grad():
    features1 = model(image1_tensor)
    features2 = model(image2_tensor)

# Calcular a similaridade coseno entre os vetores de características
cosine_similarity = F.cosine_similarity(features1, features2).item()
print(f"Similaridade Coseno: {cosine_similarity}")
