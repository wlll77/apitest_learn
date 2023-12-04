import os

import yaml

path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "data.yaml")
def read_data():
    f = open(path, encoding='utf8')
    data = yaml.safe_load(f)
    print(data)
    return data

get_data = read_data()