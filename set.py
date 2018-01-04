# set.py

import os
import glob
import time
import config
import subprocess
import consumer_key

img_lst = os.listdir(os.path.join("/home", consumer_key.current_user, ".linuxlwp/.cache/."))

while True:
	for image in img_lst:
		# set wallpaper
		subprocess.check_output(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", "file://{0}/{1}".format(os.path.join("/home", consumer_key.current_user, ".linuxlwp/.cache/."), image)])
		time.sleep(config.config_json["frequency"])