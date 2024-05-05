import os
from PIL import Image
import numpy as np

# Define the input and output directories
input_dir = r"C:\Users\HP\OneDrive\Documents\writers"
output_dir = r"C:\Users\HP\OneDrive\Documents\writers_augmented"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# Loop through all the images in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        input_image = Image.open(os.path.join(input_dir, filename))
        width, height = input_image.size
        augmented_images = np.zeros((3, height, width, 3), dtype=np.uint8)
        # Rotate the input image by 10 degrees clockwise
        augmented_images[0] = np.array(input_image.rotate(10))
        # Rotate the input image by 10 degrees anticlockwise
        augmented_images[1] = np.array(input_image.rotate(-10))
        # Zoom out the input image by 75%
        output_width = int(width * 0.75)
        output_height = int(height * 0.75)
        zoomed_out_image = input_image.resize((output_width, output_height))
        background = Image.new('RGB', (width, height), (255, 255, 255))
        x = int((width - output_width) / 2)
        y = int((height - output_height) / 2)
        background.paste(zoomed_out_image, (x, y))
        augmented_images[2] = np.array(background)

        # Save the augmented images to the output directory
        for i, image in enumerate(augmented_images):
            output_filename = os.path.splitext(filename)[0] + "_{}.png".format(i)
            output_path = os.path.join(output_dir, output_filename)
            Image.fromarray(image).save(output_path)
