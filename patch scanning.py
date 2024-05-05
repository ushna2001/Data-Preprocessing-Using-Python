import os
from PIL import Image

# Define the input and output directories
input_dir = r"C:\Users\HP\OneDrive\Documents\fyp_aaminah\HS_filtered"
output_dir = r"C:\Users\HP\OneDrive\Documents\fyp_aaminah\HS1"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# Loop through all the images in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        input_image = Image.open(os.path.join(input_dir, filename))
        width, height = input_image.size

        # Loop through the image in 256*256 fragments and save each fragment as a separate image
        for i in range(0, width, 256):
            for j in range(0, height, 256):
                box = (i, j, i+256, j+256)
                output_image = input_image.crop(box)
                output_filename = os.path.splitext(filename)[0] + "_{}_{}.png".format(i, j)
                output_path = os.path.join(output_dir, output_filename)
                output_image.save(output_path)


