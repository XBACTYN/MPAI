import json
from skimage.io import imread, imsave

settings = {
    'source_path': 'C:/Users/user/Desktop/rainbow.jpg',
    'result_path': '',
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

path = json_data['source_path']
img = imread(path)
print('Image shape: ', img.shape)

