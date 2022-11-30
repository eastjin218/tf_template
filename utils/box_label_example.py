import os ,glob, json
from collections import defaultdict

convert_dict = {
    'fish_trout_1':1,'fish_trout_2':2,'fish_trout_3':3,
    'fish_san_1':4, 'fish_san_2':5, 'fish_san_3':6
}

with open('/home/tf_template/test_v2.csv', 'r') as f:
    tmp_file = f.readlines()

img_path =glob.glob('/home/tf_template/data/*.jpg')
img_path = [os.path.basename(i) for i in img_path]
print(len(img_path))

data_dict = defaultdict(list)
for i in tmp_file[1:]:
    i = i.strip()
    if i.split(',')[0] in img_path:
        data_dict[i.split(',')[0]].append(i.split(',')[-5:])

with open('/home/tf_template/data/metadata.jsonl', 'w') as f:
    for fn, data in data_dict.items():
        file_dict = {}
        box_label_dict = defaultdict(list)
        for i in data:
            box_label_dict['bbox'].append(list(map(int,i[1:])))
            box_label_dict['categories'].append(convert_dict[i[0]])
        file_dict['file_name']=fn
        file_dict['objects']=dict(box_label_dict)
        json.dump(file_dict, f)