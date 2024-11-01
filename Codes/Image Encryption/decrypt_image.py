# decrypt_image.py
import os

KEY = 123  # Simple XOR key


def load_encrypted_text(filename):
    """Read encrypted text from a file and convert to binary data."""
    with open(filename, "r", encoding="utf-8") as text_file:
        encrypted_text = text_file.read()
    return bytes.fromhex(encrypted_text)


def xor_decrypt(data, key):
    """Decrypt binary data using XOR encryption."""
    return bytes([b ^ key for b in data])


def binary_to_image(binary_data, output_path):
    """Write binary data to an image file."""
    with open(output_path, "wb") as image_file:
        image_file.write(binary_data)


# Main script
if __name__ == "__main__":
    # Prompt user for the encrypted .txt filename
    txt_name = input(
        "Enter the name of the encrypted .txt file (in 'decrypted images' folder, include extension): ")
    txt_path = os.path.join("decrypted images", txt_name)

    if not os.path.exists(txt_path):
        print(
            f"Error: {txt_name} does not exist in 'decrypted images' folder.")
    else:
        # Load encrypted text, decrypt it, and save as an image
        encrypted_data = load_encrypted_text(txt_path)
        decrypted_data = xor_decrypt(encrypted_data, KEY)

        # Save the decrypted image in 'decrypted images' folder
        decrypted_filename = os.path.join(
            "decrypted images", f"{os.path.splitext(txt_name)[0]}_decrypted.png")
        binary_to_image(decrypted_data, decrypted_filename)

        print(f"Decryption complete. Image saved as '{decrypted_filename}'.")
