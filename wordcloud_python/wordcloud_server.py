from flask import Flask, request, jsonify
import base64
from io import BytesIO
from PIL import Image
import os

app = Flask(__name__)

# Folder to store images temporarily
IMAGE_FOLDER = "static/images"
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

@app.route('/upload_wordcloud', methods=['POST'])
def upload_wordcloud():
    data = request.json
    if 'image_base64' not in data:
        return jsonify({'error': 'No image_base64 provided'}), 400

    # Decode the base64 string
    image_data = base64.b64decode(data['image_base64'])
    image = Image.open(BytesIO(image_data))

    # Save image as PNG
    image_path = os.path.join(IMAGE_FOLDER, 'wordcloud.png')
    image.save(image_path, 'PNG')

    # Return the URL to access the image
    return jsonify({'image_url': f'http://127.0.0.1:5000/{image_path}'})

if __name__ == '__main__':
    app.run(debug=True)
