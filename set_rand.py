# set_rand.py

import os
import glob
import time
import config
import subprocess
import consumer_key
from random import randint


# print("len(img_lst)")
# print(len(img_lst))

while True:
	img_lst = os.listdir(os.path.join("/home", consumer_key.current_user, ".linuxlwp/.cache/."))
	rand_int = randint(0, len(img_lst) - 1)
	# print("rand_int")
	# print(rand_int)
	# print("============")
	print("Setting wallpaper: {0}".format(img_lst[rand_int]))
	subprocess.check_output(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", "file://{0}/{1}".format(os.path.join("/home", consumer_key.current_user, ".linuxlwp/.cache/."), img_lst[rand_int])])
	time.sleep(config.config_json["frequency"])