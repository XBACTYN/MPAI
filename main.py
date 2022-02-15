import json

from matplotlib import pyplot as plt
from skimage.color import rgb2gray
from skimage.exposure import histogram
from skimage.io import imread, imsave
from skimage.io import imshow
from skimage.segmentation import flood_fill

settings = {
    'source_path': 'C:/Users/user/Desktop/MPAILab1/flower.jpg',
    'result_path': 'C:/Users/user/Desktop/MPAILab1/flower2.jpg',
    'positionX': 540,
    'positionY': 587,
    'brightness': 0.5
}

with open('settings.json', 'w') as fp:
    json.dump(settings, fp)

with open('settings.json') as json_file:
    json_data = json.load(json_file)

for entry in json_data.keys():
    print(
        f'Название параметра: {entry},тип параметра: {type(json_data[entry])}, значение параметра: {json_data[entry]}')

path = json_data['source_path']  # Блок отвечает за чтение старого и сохранение нового изобр
# img = rgb2gray(imread(path)).astype(np.uint8)
img = rgb2gray(imread(path))
print('Image shape: ', img.shape)
filled_img = flood_fill(img, (json_data['positionX'], json_data['positionY']), json_data['brightness'], tolerance=0.3)
imsave(json_data['result_path'], filled_img)

fig = plt.figure(figsize=(12, 8))  # Блок отвечает за вывод изображения
fig.add_subplot(2, 2, 1)
imshow(img, cmap=plt.cm.gray)
fig.add_subplot(2, 2, 2)
imshow(filled_img, cmap=plt.cm.gray)


hist_red, bins_red = histogram(img)
hist_green, bins_green = histogram(img)
hist_blue, bins_blue = histogram(img)

fig.add_subplot(2, 2, 3)
plt.ylabel('Число отсчетов')
plt.ylabel('Значение яркости')
plt.title('Гистограмма распределения ярокстей по каждому каналу')
plt.plot(bins_green, hist_green, color='green', linestyle='-', linewidth=1)
plt.plot(bins_red, hist_red, color='red', linestyle='-', linewidth=1)
plt.plot(bins_blue, hist_blue, color='blue', linestyle='-', linewidth=1)
plt.legend(['green', 'red', 'blue'])

hist_red, bins_red = histogram(filled_img)
hist_green, bins_green = histogram(filled_img)
hist_blue, bins_blue = histogram(filled_img)
fig.add_subplot(2, 2, 4)
plt.ylabel('Число отсчетов')
plt.ylabel('Значение яркости')
plt.title('Гистограмма распределения ярокстей по каждому каналу')
plt.plot(bins_green, hist_green, color='green', linestyle='-', linewidth=1)
plt.plot(bins_red, hist_red, color='red', linestyle='-', linewidth=1)
plt.plot(bins_blue, hist_blue, color='blue', linestyle='-', linewidth=1)
plt.legend(['green', 'red', 'blue'])


plt.show()
