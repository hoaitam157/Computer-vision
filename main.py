from PIL import Image
import os
from imgtools import *

def load_img(img_path):
    try:
        img = Image.open(img_path)
        return img
    except Exception as e:
        print ("Loi khi doc anh tu: ", img_path)
        return None

def is_image_file(file_path):
    # return true -- neu la anh
    # return false -- neu khac anh
    extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
    return file_path.lower().endswith(extensions)

def get_img_list(folder_path):
    img_list = []
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        filenames = os.listdir(folder_path)
        for filename in filenames:
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and is_image_file(file_path):
                img = load_img(file_path)
                img_list.append(img)
    return img_list


dir = "F:\pythonProject\img"

imgs = get_img_list(dir)

for img in imgs:
    img.show()


