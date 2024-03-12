from flask import Flask, render_template, request, send_file
from PIL import Image
from io import BytesIO
from utils import encode_message, decode_message

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image/encode', methods=['POST'])
def encode_image():
    image_file = request.files['file']
    message = request.form['message']

    if image_file and message:
        try:
            result = encode_message(image_file, message)
            encoded_image_data = BytesIO()
            result.save(encoded_image_data, format='PNG')
            encoded_image_data.seek(0)
            encoded_image_data_path = "static/images/encoded_image.png"
            with open(encoded_image_data_path, "wb") as file:
                file.write(encoded_image_data.getvalue())
            return send_file(encoded_image_data_path, attachment_filename='encoded_image.png', as_attachment=True)
        except ValueError as e:
            return str(e)

    return "Error: Image file and/or message were not provided."

@app.route('/image/last/encoded')
def get_last_encoded_image():
    encoded_image_path = "static/images/encoded_image.png"
    try:
        with open(encoded_image_path, "rb") as file:
            return send_file(BytesIO(file.read()), attachment_filename='encoded_image.png', as_attachment=True)
    except FileNotFoundError:
        return "Error: No encoded image available."

@app.route('/image/decode', methods=['POST'])
def decode_image():
    image_file = request.files['file']

    if image_file:
        try:
            result = decode_message(image_file)
            decoded_message_path = "static/decoded_message.txt"
            with open(decoded_message_path, "w") as file:
                file.write(result)
            return result
        except ValueError as e:
            return str(e)

    return "Error: Image file was not provided."

@app.route('/image/last/decoded')
def get_last_decoded_message():
    decoded_message_path = "static/decoded_message.txt"
    try:
        with open(decoded_message_path, "r") as file:
            decoded_message = file.read()

        return decoded_message
    except FileNotFoundError:
        return "Error: No decoded message available."

if __name__ == '__main__':
    app.run()
