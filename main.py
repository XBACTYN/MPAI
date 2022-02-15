import json

import numpy as np
import imageio

from skimage import data, filters, color, morphology
from skimage.color import rgb2gray
from skimage.segmentation import flood, flood_fill
from skimage.io import imread, imsave
from matplotlib import pyplot as plt
from skimage.io import imshow, show
from skimage.exposure import histogram


settings = {
    'source_path': 'C:/Users/user/Desktop/MPAILab1/hat.jpg',
    'result_path': 'C:/Users/user/Desktop/MPAILab1/hat2.jpg',
    'positionX': 30,
    'positionY': 30,
    'color': ''
}

with open ('settings.json', 'w') as fp:
    json.dump(settings, fp)

with open ('settings.json') as json_file:
    json_data = json.load(json_file)

for entry in json_data.keys():
    print(f'Название параметра: {entry},тип параметра: {type(json_data[entry])}, значение параметра: {json_data[entry]}')

path = json_data['source_path']     #Блок отвечает за чтение старого и сохранение нового изобр
#img = rgb2gray(imread(path)).astype(np.uint8)
img = rgb2gray(imread(path))
print('Image shape: ', img.shape)
filled_img = flood_fill(img, (250, 1000), 0.5, tolerance=0.15)
imsave(json_data['result_path'], filled_img)


fig = plt.figure(figsize = (10,5))  # Блок отвечает за вывод изображения
fig.add_subplot(1, 2, 1)
imshow(img,cmap = plt.cm.gray)
fig.add_subplot(1, 2, 2)
imshow(filled_img,cmap = plt.cm.gray)
plt.show()

hist_red, bins_red = histogram(img[500:600,300:400])
hist_green, bins_green = histogram(img[500:600,300:400])
hist_blue, bins_blue = histogram(img[500:600,300:400])

fig2 = plt.figure(figsize = (10, 5))
plt.ylabel('Число отсчетов')
plt.ylabel('Значение яркости')
plt.title('Гистограмма распределения ярокстей по каждому каналу')
plt.plot(bins_green, hist_green,color='green', linestyle = '-', linewidth = 1)
plt.plot(bins_red, hist_red,color='red', linestyle = '-', linewidth = 1)
plt.plot(bins_blue, hist_blue,color='blue', linestyle = '-', linewidth = 1)
plt.legend(['green', 'red', 'blue'])
plt.show()
