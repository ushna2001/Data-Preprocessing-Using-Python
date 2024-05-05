import os
import random
import shutil

src_dir = r"C:\Users\HP\OneDrive\Documents\Patch_Scanning\UA_scanned_images"
train_dir = os.path.join(src_dir, "Train")
test_dir = os.path.join(src_dir, "Test")

os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

files = os.listdir(src_dir)

# Calculate the number of files for training and testing
num_files = len(files)
num_train = int(0.8 * num_files)
num_test = num_files - num_train

# Randomly select files for training and testing
train_files = random.sample(files, num_train)
test_files = [file for file in files if file not in train_files]

# Copy the train files to the train directory
for file in train_files:
    src_path = os.path.join(src_dir, file)
    dst_path = os.path.join(train_dir, file)
    try:
        shutil.copy(src_path, dst_path)
    except IOError as e:
        print("Unable to copy file '{}': {}".format(file, e))

# Copy the test files to the test directory
for file in test_files:
    src_path = os.path.join(src_dir, file)
    dst_path = os.path.join(test_dir, file)
    try:
        shutil.copy(src_path, dst_path)
    except IOError as e:
        print("Unable to copy file '{}': {}".format(file, e))
