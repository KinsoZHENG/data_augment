import os

path_ori = "/home/kinsozheng/Desktop/data_augment/train/"
path_mask_ori = "/home/kinsozheng/Desktop/data_augment/mask/"

aug_ori = "/home/kinsozheng/Desktop/data_augment/tmp/train/"
aug_mask = "/home/kinsozheng/Desktop/data_augment/tmp/mask/"

ori_image = os.listdir(path_ori)
ori_mask = os.listdir(path_mask_ori)

aug_image = os.listdir(aug_ori)
aug_path_mask = os.listdir(aug_mask)

print(ori_image.__len__())
print(ori_mask.__len__())
print(aug_image.__len__())
print(aug_path_mask.__len__())

from PIL import Image

im_path = "/home/kinsozheng/Desktop/data_augment/train/EAD2020_semantic_00000.jpg"
im_PIL = Image.open(im_path)
x1, x2 = im_PIL.size
print(x1, x2)

x1, x2 = int(x1 / 2), int(x2 / 2)
print(x1, x2)
