# KV Store Editor

Contains scripts that allow basic POST/GET/DELETE operations on local Splunks KV Store

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Have python3 interpretor on system.

### Instal/Running

* Add local splunk user and password to `settings.json`
* Run `setup.sh` to create virtual environments and install libraries
* Run `run.sh` to clear and post the data defaults to the kvstore

### Editing

* Topology data is stored in `topology.json`
* Splunk/Post options (user/pword) are retrieved from `settings.json`

## KV Store Scripts

Run one of these scripts:
* `get_all.py`
* `post_all.py`
* `delete_all.py`
