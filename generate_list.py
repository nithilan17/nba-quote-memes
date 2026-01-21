import os

# Define the folder and valid extensions
images_folder = 'images'
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp')

# Get all valid image files and sort them to maintain order
files = sorted([f for f in os.listdir(images_folder) 
                if f.lower().endswith(image_extensions)])

# Write the formatted list to images.txt
with open('images.txt', 'w') as f:
    f.write("const imageFiles = [\n")
    for file in files:
        f.write(f"    '{file}',\n")
    f.write("];")

print("Successfully created images.txt with the list of images.")