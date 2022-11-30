import datetime
import math
import datasets
import tensorflow as tf

from tqdm import tqdm, tnrange

def get_time():
    return datetime.datetime.now()

def load_img_dataset(path, split_rate, seed ):
    ds = datasets.load_dataset(path)
    ds = ds.shuffle(seed=1)
    ds = ds['train'].train_test_split(test_size=split_rate, seed=seed)
    train_ds = ds['train']
    test_ds = ds['test']
    return train_ds, test_ds

def resize_img(image: tf.Tensor, resize:int)->tf.Tensor:
    return tf.image.resize(image, (resize, resize))

def write_cls_tfrecords(root_dir, dataset, split, batch_size, resize):
    print(f"Preparing TFRecords for split: {split}.")

    for step in tnrange(int(math.ceil(len(dataset) / batch_size))):
        temp_ds = dataset[step * batch_size : (step + 1) * batch_size]
        shard_size = len(temp_ds["image"])
        filename = os.path.join(
            root_dir, "{}-{:02d}-{}.tfrec".format(split, step, shard_size)
        )

        with tf.io.TFRecordWriter(filename) as out_file:
            for i in range(shard_size):
                image = temp_ds["image"][i]
                label = temp_ds["labels"][i]
                example = create_tfrecord(image, label, resize)
                out_file.write(example)
            print("Wrote file {} containing {} records".format(filename, shard_size))

def write_ob_tfrecords(root_dir, dataset, split, batch_size, resize):
    print(f"Preparing TFRecords for split: {split}.")

    for step in tnrange(int(math.ceil(len(dataset) / batch_size))):
        temp_ds = dataset[step * batch_size : (step+1)*batch_size]
        shard_size = len(temp_ds['image'])

        with tf.io.TFRecordWriter(filename) as out_file:
            for i in range(shard_size):
                image = temp_ds["image"][i]
                label = temp_ds[""]