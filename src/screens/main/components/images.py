# Arquivo para modificar imagens

from PIL import Image

image1 = Image.open("src/assets/images/cheers.png") 
image2 = Image.open("src/assets/images/cheers2.png")

# Redimensionar a imagem para um novo tamanho (por exemplo, 200x200)
new_size = (200, 200)
resized_image1 = image1.resize(new_size)
resized_image2 = image2.resize(new_size)

# Salvar a imagem redimensionada
resized_image1.save("src/assets/images/rd_cheers.png") 
resized_image2.save("src/assets/images/rd_cheers2.png") 