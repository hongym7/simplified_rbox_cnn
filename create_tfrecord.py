'''
import os
path = '/mnt/disk2/dl_data/Arirang_Dataset/train/json/'
files = os.listdir(path)
print('json 파일 총 개수 :', len(files))


import json

all_json = None

for file in files:
    json_data = json.load(open(path + file))

    if all_json is None:
        all_json = json_data
    else:
        all_json['features'].extend(json_data['features'])

with open('/mnt/disk2/dl_data/Arirang_Dataset/train/labels.json', 'w') as outfile:
    json.dump(all_json, outfile, indent='\t')
'''



