import os
import platform
import ctypes

res = requests.get(f"https://api.unsplash.com/photos/random?client_id={APIKEY}")