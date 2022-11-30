import os, glob, argparse, sys
import tensorflow as tf
import numpy as np
from typing import Tuple
from tqdm import tqdm
from PIL import Image

sys.path.append('./../')
from util import load_img_dataset

img_dir = '/home/tf_template/data'
train_ds, test_ds = load_img_dataset(img_dir, split_rate=0.2, seed=1)
print(train_ds[:10]['image'])
print(train_ds[:10]['objects'])