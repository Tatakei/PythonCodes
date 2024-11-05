from PIL import Image
import os

# Set the input and output folder paths automatically
input_folder = "C:/Users/Sascha/Desktop/Python/PythonCodes/Codes/ImageConverter/ImgResizer/Png"
output_folder = "C:/Users/Sascha/Desktop/Python/PythonCodes/Codes/ImageConverter/ImgResizer/ResizedPng"

# Desired size (width, height)
# desired_size = input("Size? (ex. (800, 600))")
desired_size = (166, 200)

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png")):  # Check for image files
        input_path = os.path.join(input_folder, filename)
        output_filename = f"resized_{os.path.splitext(
            filename)[0]}.png"  # Change file extension to .png
        output_path = os.path.join(output_folder, output_filename)

        # Resize the image
        try:
            img = Image.open(input_path)
            # Use LANCZOS for high-quality resizing
            img_resized = img.resize(desired_size, Image.Resampling.LANCZOS)
            img_resized.save(output_path)  # Save the resized image
            print(f"Resized '{filename}' and saved as '{
                  output_filename}' at '{output_path}'")
        except Exception as e:
            print(f"An error occurred while processing '{filename}':", e)
