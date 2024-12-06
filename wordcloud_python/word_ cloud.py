import requests
import json

# Set up data for the word cloud
keywords = ["data", "science", "machine", "learning", "AI"]
tfidf_scores = [0.9, 0.7, 0.6, 0.8, 0.5]

# Send the request to TabPy
url = "http://localhost:9004/query/generate_wordcloud"
payload = json.dumps({"keywords": keywords, "tfidf_scores": tfidf_scores})
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=payload, headers=headers)
result = response.json()

# Decode and save the image if the result is base64
if 'response' in result:
    img_base64 = result['response']
    with open("wordcloud_output.png", "wb") as img_file:
        img_file.write(base64.b64decode(img_base64))
    print("Word cloud image saved as 'wordcloud_output.png'.")
else:
    print("Error generating word cloud:", result)
