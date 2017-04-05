#!/usr/bin/env python

import yaml
import json

def main():
    yaml_collection = 'startrek.yml'
    json_collection = 'startrek.json'
    with open(yaml_collection) as f:
        startrek_yml = yaml.load(f)
    with open(json_collection) as f:
        startrek_json = json.load(f)
    print startrek_yml
    print startrek_json

if __name__ == "__main__":
    main()
