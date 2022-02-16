import json

from matplotlib import pyplot as plt
from skimage.color import rgb2gray
from skimage.exposure import histogram
from skimage.io import imread, imsave
from skimage.io import imshow
from skimage.segmentation import flood_fill

settings = {
    'source_path': 'C:/Users/user/Desktop/MPAILab1/revy.jpg',
    'result_path': 'C:/Users/user/Desktop/MPAILab1/revy2.jpg',
    'positionX': 150,
    'positionY': 1640,
    'brightness': 0.5,
    'tolerance': 0.1
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
filled_img = flood_fill(img, (json_data['positionX'], json_data['positionY']), json_data['brightness'], tolerance = json_data['tolerance'])
imsave(json_data['result_path'], filled_img)

fig = plt.figure(figsize=(12, 8))  # Блок отвечает за вывод изображения
fig.add_subplot(2, 2, 1)
imshow(img, cmap=plt.cm.gray)
fig.add_subplot(2, 2, 2)
imshow(filled_img, cmap=plt.cm.gray)


hist_brightness, bins_brightness = histogram(img)


fig.add_subplot(2, 2, 3)
plt.plot(bins_brightness, hist_brightness, color='black', linestyle='-', linewidth=1)
plt.legend(['brightness'])

hist_brightness, bins_brightness = histogram(filled_img)

fig.add_subplot(2, 2, 4)
plt.plot(bins_brightness, hist_brightness, color='black', linestyle='-', linewidth=1)
plt.legend(['brightness'])


plt.show()
