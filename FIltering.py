import os
from PIL import Image, ImageFilter

# Set the directory containing the padded images
padded_dir_path = r"C:\Output\White Pixel Padding\AB_padded_images"

# Create a new directory for the filtered images
filtered_dir_path = os.path.join(padded_dir_path, "filtered_images")
os.makedirs(filtered_dir_path, exist_ok=True)

# Loop through the padded images in the directory and apply a filter
for filename in os.listdir(padded_dir_path):
    if filename.endswith(".jpg") or filename.endswith(".png")
        img = Image.open(os.path.join(padded_dir_path, filename))
        filtered_img = img.filter(ImageFilter.MedianFilter(size=3))
        new_filename =  filename
        new_filepath = os.path.join(filtered_dir_path, new_filename)
        filtered_img.save(new_filepath)
