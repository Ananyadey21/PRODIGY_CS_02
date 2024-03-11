from PIL import Image

def encrypt_image(input_path, output_path, key):
    # Open the image
    img = Image.open(input_path)
    pixels = img.load()

    # Encrypt the image using modular addition
    width, height = img.size
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Example: Encrypt each pixel value using modular addition
            encrypted_r = (r + key) % 256
            encrypted_g = (g + key) % 256
            encrypted_b = (b + key) % 256

            # Update the pixel value
            pixels[i, j] = (encrypted_r, encrypted_g, encrypted_b)

    # Save the encrypted image
    img.save(output_path)

# Example usage
input_image_path = "C:\\Users\\anany\\OneDrive\\Desktop\\Prodigy\\mee2.jpg"
output_image_path = "C:\\Users\\anany\\OneDrive\\Desktop\\Prodigy\\encrypted_image.jpg"
encryption_key = 50

encrypt_image(input_image_path, output_image_path, encryption_key)