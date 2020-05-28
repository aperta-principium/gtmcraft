import os
import time

delay = 60
delay = delay * 60

def updt():
    os.system("git pull")
    os.system("git add .")
    os.system('git commit -m "Update worlds")
    os.system("git push")
    time.sleep(delay)
    updt()
updt()