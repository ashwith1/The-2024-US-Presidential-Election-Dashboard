import requests
import json

url = "http://127.0.0.1:5000/upload_wordcloud"
data = {
    "image_base64": "your_base64_string"  # Replace with actual base64 image string
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.json())
