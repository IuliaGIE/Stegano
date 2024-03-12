from PIL import Image

def encode_message(image_file, message):
    try:
        image = Image.open(image_file)
        pixels = list(image.getdata())

        binary_message = ""
        for char in message:
            binary_char = bin(ord(char))[2:].zfill(8)
            binary_message += binary_char

        if len(binary_message) > len(pixels) * 3:
            raise ValueError("Error: The message is too long to be hidden in the selected image.")

        encoded_pixels = []
        for i, pixel in enumerate(pixels):
            if i * 3 < len(binary_message):
                encoded_pixel = []
                for j, channel in enumerate(pixel):
                    if j < 3:
                        encoded_channel = (channel & 0xFE) | int(binary_message[i * 3 + j])
                        encoded_pixel.append(encoded_channel)
                    else:
                        encoded_pixel.append(channel)
                encoded_pixels.append(tuple(encoded_pixel))
            else:
                encoded_pixels.append(pixel)

        encoded_image = Image.new(image.mode, image.size)
        encoded_image.putdata(encoded_pixels)

        encoded_image_path = "static/images/encoded_image.png"
        encoded_image.save(encoded_image_path)

        return encoded_image_path

    except Exception as e:
        raise ValueError("Error: Failed to hide the message in the image.") from e

def decode_message(image_file):
    try:
        image = Image.open(image_file)
        pixels = list(image.getdata())

        binary_message = ""
        for pixel in pixels:
            for channel in pixel[:3]:
                binary_channel = bin(channel)[-1]
                binary_message += binary_channel

        message = ""
        for i in range(0, len(binary_message), 8):
            byte = binary_message[i:i+8]
            ...
            # Restul codului pentru decodificarea mesajului

    except Exception as e:
        raise ValueError("Error: Failed to decode the message from the image.") from e

