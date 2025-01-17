from PIL import Image
import numpy as np
import os

def create_sample_images(dir, num_images=10, image_size=(256, 256), mode='RGB'):
    os.makedirs(dir, exist_ok=True)
    for i in range(num_images):
        img_array = np.random.rand(*image_size, 3) * 255
        img = Image.fromarray(img_array.astype('uint8')).convert(mode)
        img.save(os.path.join(dir, f'image_{i:04d}.png'))

def create_sample_masks(dir, num_images=10, image_size=(256, 256), mode='RGB'):
    os.makedirs(dir, exist_ok=True)
    for i in range(num_images):
        img_array = np.random.rand(*image_size, 3) * 255
        img = Image.fromarray(img_array.astype('uint8'))
        img.save(os.path.join(dir, f'mask_{i:04d}.png'))


input_dir = './datasets/random_dataset/images'
target_dir = './datasets/random_dataset/masks'

create_sample_images(input_dir)
create_sample_masks(target_dir)
