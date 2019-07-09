#!/usr/bin/env python3
import requests
import json

with open("settings.json") as f:
    settings = json.load(f)


url = settings["splunk-base"] + "servicesNS/nobody/acn_mywizard360_aiops_sh/storage/collections/data/data_topology"

payload = ""
headers = {
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "localhost:8089",
    'Connection': "keep-alive",
    'cache-control': "no-cache",
    }

response = requests.request("GET", url, data=payload, headers=headers, verify=False, auth=(settings["user"], settings["password"]))

print("\nSTATUS: {}".format(response.status_code))
print("\nRESPONSE: ")
try:
	print(json.dumps(json.loads(response.text), indent=4, sort_keys=True))
except json.decoder.JSONDecodeError as e:
	print(response.text)
