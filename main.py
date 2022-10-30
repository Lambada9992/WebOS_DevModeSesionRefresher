import os
import requests

WEBOS_DEV_TOKEN = os.getenv('WEBOS_DEV_TOKEN')
URL = 'https://developer.lge.com/secure/ResetDevModeSession.dev?sessionToken='

if __name__ == "__main__":
    requests.get(URL + WEBOS_DEV_TOKEN)