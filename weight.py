#!/usr/bin/env python3

""" Python script to read and safe config json """

import json

config = {}
config['client_id'] = 'aaaa'
config['client_secret'] = 'bbbb'

with open("config.json", "w") as outfile:
    _json = json.dumps(config, indent=4)
    outfile.write(_json)

with open('config.json', 'r') as openfile:

    config = json.load(openfile)

    print(config)
