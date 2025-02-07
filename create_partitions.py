import os
import shutil
import random

# Define paths
input_dir = "Agricultural-crops/"  # Change this to the folder where your images are stored
output_dir = "Agricultural-crops_ML/"   # Change this to where you want the train/test folders

# Train-Test split ratio
train_ratio = 0.8

# Create train and test directories
train_dir = os.path.join(output_dir, "train")
test_dir = os.path.join(output_dir, "test")

# Ensure output folders exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Loop through each class folder in the dataset
for class_name in os.listdir(input_dir):
    class_path = os.path.join(input_dir, class_name)
    
    if not os.path.isdir(class_path):
        continue  # Skip files, process only folders
    
    # Get list of all images in class folder
    images = [f for f in os.listdir(class_path) if os.path.isfile(os.path.join(class_path, f))]
    
    # Shuffle the images randomly
    random.shuffle(images)
    
    # Compute split index
    split_idx = int(len(images) * train_ratio)
    
    # Partition into train and test sets
    train_images = images[:split_idx]
    test_images = images[split_idx:]
    
    # Create class directories in train and test
    train_class_dir = os.path.join(train_dir, class_name)
    test_class_dir = os.path.join(test_dir, class_name)
    
    os.makedirs(train_class_dir, exist_ok=True)
    os.makedirs(test_class_dir, exist_ok=True)

    # Move images to the respective train/test directories
    for img in train_images:
        shutil.copy(os.path.join(class_path, img), os.path.join(train_class_dir, img))

    for img in test_images:
        shutil.copy(os.path.join(class_path, img), os.path.join(test_class_dir, img))

    print(f"Processed class: {class_name} | Train: {len(train_images)} | Test: {len(test_images)}")

print("Dataset successfully partitioned into train and test sets.")
