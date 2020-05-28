import subprocess
import os

os.system('start start.bat')
os.system('start changeip.bat')
os.system('D:/Downloads/ngrok-stable-windows-amd64/ngrok.exe tcp 25565 --region=eu')
os.system('python updater.py')