#!/usr/bin/env python3
import requests
import json

with open("settings.json") as f:
    settings = json.load(f)

with open("topology.json") as f:
	payload_data = json.load(f)
payload_string = json.dumps(payload_data)




url = settings["splunk-base"] + "servicesNS/nobody/acn_mywizard360_aiops_sh/storage/collections/data/data_topology/batch_save"

payload = payload_string
headers = {
    'Content-Type': "application/json",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "localhost:8089",
    'Connection': "keep-alive",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False, auth=(settings["user"], settings["password"]))

print("\nSTATUS: {}".format(response.status_code))
print("\nRESPONSE: ")
try:
	print(json.dumps(json.loads(response.text), indent=4, sort_keys=True))
except json.decoder.JSONDecodeError as e:
	print(response.text)