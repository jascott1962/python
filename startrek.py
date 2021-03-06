#!/usr/bin/env python

import yaml
import json
def main():
    yaml_collection = 'startrek.yml'
    json_collection = 'startrek.json'
    ships_of_the_line = {
        'enterprise': 'ncc1701',
        'excelsior': 'ncc-2000',
        'voyager': 'ncc-74656',
        'prometheus': 'nx-59650'
    }
    captains_available = [
        'James T. Kirk',
        'Katherine Janeway',
        'John-Luc Pickard',
        ships_of_the_line,
        'female',
        'male'
    ]
    with open(yaml_collection, "w") as f:
        f.write(yaml.dump(captains_available, default_flow_style=False))
    with open(json_collection, "w") as f:
        json.dump(captains_available, f)


if __name__ == "__main__":
    main()
