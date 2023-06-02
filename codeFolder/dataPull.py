import os
import requests
import zipfile

# The URL where the data can be downloaded
download_link = "https://www.kaggle.com/datasets/balabaskar/tom-and-jerry-image-classification/download?datasetVersionNumber=3"

# The path where you want to save the downloaded file
download_path = "../dataFolder"

# Check if the file is already downloaded
if not os.path.exists(download_path):
    # Download the file
    response = requests.get(download_link)
    print(response.headers['Content-Type'])
    with open(download_path, 'wb') as f:
        f.write(response.content)

# The path where you want to extract the zip file
extract_path = "../dataFolder"

# Extract the zip file
with zipfile.ZipFile(download_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
