# Upload to imgBB

import base64
import requests
import sys

# Replace with your API key
api_key = 'xxx'

# Declare file name variable
file_name = ''


def upload_image(filePath):
    try:
        with open(filePath, "rb") as file:
            url = "https://api.imgbb.com/1/upload"
            payload = {
                "key": api_key,
                "image": base64.b64encode(file.read()),
                "name": file_name,
            }
            res = requests.post(url, payload)
        if res.status_code == 200:
            print("Server Response: " + str(res.status_code))
            print("Image Successfully Uploaded")
        else:
            print("ERROR")
            print("Server Response: " + str(res.status_code))
    except FileNotFoundError as e:
        print("FileNotFoundError:", e)
        sys.exit()
    except OSError as e:
        print("OSError:", e)
        sys.exit()
    except Exception as e:
        print(type(e), e)
        sys.exit()


def main():
    print("imgBB API Uploader")
    print("API Key: " + api_key)
    file_location = input("Image Location: ")
    file_name = input("Image Name: ")
    upload_image(file_location)


if __name__ == '__main__':
    main()
