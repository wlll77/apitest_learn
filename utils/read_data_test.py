import yaml

f = open("../data/data.yaml", encoding='utf8')
data = yaml.safe_load(f)

# print(data['hero'])
# print(data['heros_name'])
# print(data['heros'])
# print(data['heros_name_list'])
print(data)
print(data['test'])
print(data['test']['name'])
print(data['test']['request'])
print(data['test']['request']['url'])
print(data['test']['request']['method'])
print(data['test']['request']['headers'])
print(data['test']['request']['json'])
