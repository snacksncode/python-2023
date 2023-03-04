import numpy as np
from PIL import Image

img = Image.open("image1.jpeg")
print(img.size)
img.show()
# img2 = img.resize((300, 300))  # przeskalowujemy obrazek
# img2.show()

mm = np.array(img)
print(mm[:, :, 0])
print(mm.shape)
nn = mm * 0.25
print(nn.shape)

cc = nn.astype(dtype=np.uint8)
img3 = Image.fromarray(cc)
img3.show()
