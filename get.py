# get.py

__author__ = "Riju"
__maintainer__ = "Riju"
__email__ = "mailmeonriju@gmail.com"
__status__ = "Development"

import json
import config
import requests
import consumer_key
from os import path
from random import randint


def get():
	cnt = 0
	page = 1
	# get number of pages
	url = "{1}photos?feature={2}&page={6}&consumer_key={0}&only={3}&rpp={5}&image_size={4}".format(
			consumer_key.consumer_key, 
			config.config_json["api_endpoint"],
			config.config_json["stream"],
			",".join(config.config_json["categories"]),
			config.config_json["image_size"],
			config.config_json["max_files"],
			page,
			)
	response = requests.get(url)
	response_json = response.json()
	# print(json.dumps(response_json,indent=2))
	# exit()
	total_pages = response_json["total_pages"]
	pages_queried = []
	while cnt < config.config_json["max_files"]:
		rand_page = 0
		while rand_page == 0 or rand_page in pages_queried:
			rand_page = randint(1,total_pages)
		pages_queried.append(rand_page)
		page = rand_page
		url = "{1}photos?feature={2}&page={6}&consumer_key={0}&only={3}&rpp={5}&image_size={4}".format(
			consumer_key.consumer_key, 
			config.config_json["api_endpoint"],
			config.config_json["stream"],
			",".join(config.config_json["categories"]),
			config.config_json["image_size"],
			config.config_json["max_files"],
			page,
			)
		print("Getting {0}".format(url))
		response = requests.get(url)
		response_json = response.json()
		for image in response_json["photos"]:
			image_url_short = image["url"].split("/")[-1]
			if image["hi_res_uploaded"] != 0 and not path.isfile(path.join("/home", consumer_key.current_user, ".linuxlwp/.cache/", image_url_short + "." + image["image_format"])) and (image["nsfw"] == (False if not 'show_nsfw' in config.config_json["show_nsfw"] else config.config_json["show_nsfw"])) and cnt < config.config_json["max_files"]:
				print("Getting image: {0}".format(image_url_short))
				# print(image["image_url"])
				r_image = requests.get(image["image_url"][0])
				with open(path.join("/home", consumer_key.current_user, ".linuxlwp/.cache/", image_url_short + "." + image["image_format"]), 'wb') as fd:
				    for chunk in r_image.iter_content(chunk_size=128):
				        fd.write(chunk)
				cnt += 1
				print("cnt")
				print(cnt)
		

if __name__ == "__main__":
	get()