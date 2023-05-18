import requests

# Specify the URL of your API
url = "http://18.184.77.184/predict/"

# Open and read the image file
file = {"file": open("image.jpg", "rb")}

# Send a POST request to the API
response = requests.post(url, files=file)

# Print the response
print(response.json())
