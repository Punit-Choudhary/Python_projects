import os
import platform
import ctypes
import requests
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv("APIKEY")

res = requests.get(f"https://api.unsplash.com/photos/random?client_id={APIKEY}")
data = res.json()

file = open("image.png", "wb")
file.write(requests.get(data['urls']['regular']).content)
file.close()

def set_wallpaper():
    # Check the OS
    system_name = platform.system().lower()
    path = ''

    if system_name == 'linux':
        path = os.getcwd() + '/image.png'
        command = "gsettings set org.gnome.desktop.background picture-uri file:" + path
        os.system(command)
    elif system_name == 'windows':
        path = os.getcwd() + '\\image.png'
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

set_wallpaper()