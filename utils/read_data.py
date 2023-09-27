import yaml

f = open("../config/data.yaml", encoding='utf8')
data = yaml.safe_load(f)

print(data['hero'])
print(data['heros_name'])
print(data['heros'])
print(data['heros_name_list'])