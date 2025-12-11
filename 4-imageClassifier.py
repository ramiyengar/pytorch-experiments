import urllib.request
url = 'https://www.cloudfoundry.org/wp-content/uploads/run-your-app-isometric.png'
fpath = 'isometri.jpg'

# Create a Request object with a User-Agent header
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

try:
    # Open the URL using the Request object
    with urllib.request.urlopen(req) as response:
        # Read the content and write it to the file
        with open(fpath, 'wb') as f:
            f.write(response.read())
    print(f"Successfully downloaded {fpath}")
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
except Exception as e:
    print(f"An error occurred: {e}")

import matplotlib.pyplot as plt
from PIL import Image
img = Image.open(fpath)
plt.imshow(img)

