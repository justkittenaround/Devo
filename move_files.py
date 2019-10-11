






src_folder = ''
dst_folder = '/home/blu/DATA/cats_dogs_10k/train/cats'

import os
import numpy as np
import shutil
files = os.listdir(src_folder)
num = len(files) - 2000
og_files = []
for f in files:
    if f.startswith('cat'):
        og_files.append(f)

choices = np.random.choice(og_files, num, replace=False)
for f in og_files:
     src = src_folder + '/' + f
     dist = dst_folder + '/' + f
     shutil.move(src, dist)
