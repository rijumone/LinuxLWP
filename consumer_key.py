# consumer_key.py

import os
import subprocess

current_user = subprocess.check_output(["whoami"]).decode("utf-8").strip("\n")
consumer_key = None

with open (os.path.join("/home",current_user, ".linuxlwp/consumer_key" )) as consumer_key_file:
	consumer_key = consumer_key_file.read().strip("\n")

