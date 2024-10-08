import requests
import json

from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
api_key = os.getenv('API_KEY')

url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"
querystring = {"id": "zVSUp6EIuis"} 

headers = {
    "x-rapidapi-host": "ytstream-download-youtube-videos.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(f"Response Status Code: {response.status_code}")
data = response.json() #storing JSON

# print all JSON
print("Response JSON:", data)

# check download links
download_link_found = False

# checking download key
if 'download' in data:
    print("Download link found:", data['download'])
    download_link_found = True

# check if 'formats' key exists and iterate through it to find URLs
if 'formats' in data:
    for format_info in data['formats']:
        if 'url' in format_info:
            print("Download link found in formats:", format_info['url'])
            download_link_found = True
            break

if not download_link_found:
    print("No download link found in the response.")

# pretty JSON
print(json.dumps(data, indent=4))

# downloading first available link
download_link = data['formats'][0]['url']
response = requests.get(download_link)

# save the video to a file
with open('video.mp4', 'wb') as file:
    file.write(response.content)

print("Video downloaded successfully.")
