import os
from PIL import Image

dir_path = r"C:\Data Augmentation\AB_augmented_images"

# Create a new directory for the padded images
padded_dir_path = os.path.join(dir_path, "padded_images")
os.makedirs(padded_dir_path, exist_ok=True)

max_width = 0
for filename in os.listdir(dir_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img = Image.open(os.path.join(dir_path, filename))
        width, height = img.size
        if width > max_width:
            max_width = width

# Loop through the images in the directory 
for filename in os.listdir(dir_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img = Image.open(os.path.join(dir_path, filename))
        width, height = img.size
        padding_x = max_width - width
        padding_y = 256 - height
        new_img = Image.new('RGB', (max_width, 256), (255, 255, 255))
        x_offset = padding_x // 2
        y_offset = padding_y // 2
        new_img.paste(img, (x_offset, y_offset))
        new_filename = "padded_" + filename
        new_filepath = os.path.join(padded_dir_path, new_filename)
        new_img.save(new_filepath)
