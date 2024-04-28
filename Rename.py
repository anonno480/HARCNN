import os

def rename_images(folder_path, folder_name):
    # Get list of all files in the folder
    files = os.listdir(folder_path)
    
    # Filter out only the image files
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    
    # Enumerate through each image file and rename it
    for i, image_file in enumerate(image_files, start=1):
        _, ext = os.path.splitext(image_file)
        new_name = f"{folder_name}_image_{i}{ext}"
        os.rename(os.path.join(folder_path, image_file), os.path.join(folder_path, new_name))

# Provide the folder path where the images are located
folder_path = r"C:\Users\USER\Desktop\Research For Everyone\Walking"

# Provide the folder name
folder_name = "Walking"

# Call the function to rename images in the specified folder
rename_images(folder_path, folder_name)
