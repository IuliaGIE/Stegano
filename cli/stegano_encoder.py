from PIL import Image

def encode_message(image_file, message):
    try:
        image = Image.open(image_file)
        pixels = list(image.getdata())
        encoded_pixels = []

        # Convert the message to binary representation
        binary_message = ''.join(format(ord(char), '08b') for char in message)

        # Check if the message can be hidden in the image
        if len(binary_message) > len(pixels) * 3:
            raise ValueError("Error: The message is too long to be encoded in the image.")

        # Encode each bit of the message in the least significant bits of the RGB channels
        for i, pixel in enumerate(pixels):
            r, g, b = pixel
            if i < len(binary_message):
                msg_bit = binary_message[i]
                # Set the least significant bit of each color component based on the message bit
                r = (r & 0xFE) | int(msg_bit)
                g = (g & 0xFE) | int(msg_bit)
                b = (b & 0xFE) | int(msg_bit)
            encoded_pixels.append((r, g, b))

        encoded_image = Image.new(image.mode, image.size)
        encoded_image.putdata(encoded_pixels)

        return encoded_image

    except Exception as e:
        raise ValueError("Error: Failed to encode the message into the image.") from e
