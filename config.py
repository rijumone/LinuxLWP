# config.py

"""
Load config.json into memory
"""
import json

config_json = {}

with open("config.json") as config_json_file:
	config_json = json.loads(config_json_file.read())