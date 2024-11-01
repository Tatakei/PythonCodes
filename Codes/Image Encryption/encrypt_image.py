# encrypt_image.py
import os

KEY = 123  # Simple XOR key


def read_image_as_binary(file_path):
    """Read the image and return binary data."""
    with open(file_path, "rb") as image_file:
        binary_content = image_file.read()
    return binary_content


def xor_encrypt(data, key):
    """Encrypt binary data using XOR encryption."""
    return bytes([b ^ key for b in data])


def save_encrypted_text(data, filename):
    """Save encrypted binary data as hex text in a file."""
    with open(filename, "w", encoding="utf-8") as text_file:
        text_file.write(data.hex())


# Main script
if __name__ == "__main__":
    # Prompt user for the image filename
    image_name = input(
        "Enter the name of the image to encrypt (in 'encrypted images' folder, include extension): ")
    image_path = os.path.join("encrypted images", image_name)

    if not os.path.exists(image_path):
        print(
            f"Error: {image_name} does not exist in 'encrypted images' folder.")
    else:
        # Read image, encrypt it, and save the result as text
        image_data = read_image_as_binary(image_path)
        encrypted_data = xor_encrypt(image_data, KEY)

        # Save the encrypted data in 'decrypted images' folder
        encrypted_filename = os.path.join(
            "decrypted images", f"{os.path.splitext(image_name)[0]}_encrypted.txt")
        save_encrypted_text(encrypted_data, encrypted_filename)

        print(f"Decryption complete. Image saved as '{encrypted_filename}'.")
