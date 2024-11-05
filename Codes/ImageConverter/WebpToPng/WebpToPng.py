"""
"""
import os
from PIL import Image

# Set the input and output folder paths automatically
input_folder = "C:/Users/Sascha/Desktop/Python/PythonCodes/Codes/ImageConverter/WebpToPng/Images/Webp"
output_folder = "C:/Users/Sascha/Desktop/Python/PythonCodes/Codes/ImageConverter/WebpToPng/Images/Png"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".webp"):  # Check for .webp files
        input_path = os.path.join(input_folder, filename)
        # Change file extension to .png
        output_filename = f"{os.path.splitext(filename)[0]}.png"
        output_path = os.path.join(output_folder, output_filename)

        # Open the WebP image and save it as a PNG
        try:
            img = Image.open(input_path)
            img.save(output_path, "PNG")
            print(f"Converted '{filename}' to '{
                  output_filename}' and saved at '{output_path}'")
        except Exception as e:
            print(f"An error occurred while converting '{filename}':", e)
