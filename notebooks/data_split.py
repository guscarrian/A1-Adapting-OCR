import os
import random

# Defining the paths for the source folder and the destination folders (train and test folders):
source_folder = "/home/guscarrian@GU.GU.SE/A1-Adapting-OCR/carplates_dataset/LP-characters/images"
train_folder = "/home/guscarrian@GU.GU.SE/A1-Adapting-OCR/carplates_dataset/LP-characters/train_images"
test_folder = "/home/guscarrian@GU.GU.SE/A1-Adapting-OCR/carplates_dataset/LP-characters/test_images"

# Creating the train and test folders in case they don't exist and getting list of image files:
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)
img_files = os.listdir(source_folder)
#print('IMG_FILES: ', img_files)

# Setting the random seed for reproducibility, shuffling the imafe files and splitting train/test (80/20):
random.seed(42)
random.shuffle(img_files)
split_index = int(0.8 * len(img_files))
train_img_files = img_files[:split_index]
test_img_files = img_files[split_index:]

# Moving the train images to the training folder:
for img_file in train_img_files:
 source = os.path.join(source_folder, img_file)
 train_set = os.path.join(train_folder, img_file)
 os.rename(source, train_set)

# Moving the test images to the test folder:
for img_file in test_img_files:
 source = os.path.join(source_folder, img_file)
 test_set = os.path.join(test_folder, img_file)
 os.rename(source, test_set)

print(f"Total images: {len(img_files)}")
print(f"Traininig data size: {len(train_img_files)}")
print(f"Test data size: {len(test_img_files)}")
