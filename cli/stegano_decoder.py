from PIL import Image

def decode_message(image_file):
    try:
        image = Image.open(image_file)
        pixels = image.getdata()

        message = ""
        for pixel in pixels:
            r, g, b = pixel
            # Extract the least significant bit from each color channel
            msg_bit = bin(r)[-1] + bin(g)[-1] + bin(b)[-1]
            char = chr(int(msg_bit, 2))
            message += char

        return message

    except Exception as e:
        raise ValueError("Error: Failed to decode the message from the image.") from e
