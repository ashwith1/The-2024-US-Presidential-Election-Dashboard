import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Use this function to get the base64 string of an image
image_base64_string = image_to_base64("path/to/your/image.png")
print(image_base64_string)