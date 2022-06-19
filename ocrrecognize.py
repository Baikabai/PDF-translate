import pytesseract
from PIL import Image
import os


def recognize_text(image_path):
    output = 'output.txt'
    name_list = os.listdir(image_path)
    with open(output,'w') as f:
        for img_name in name_list:
            image = Image.open(img_name)
            text = pytesseract.image_to_string(image,lang='jpn')
            f.write(text)
        f.close()

