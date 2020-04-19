
import json
from pprint import pprint
from collections import defaultdict, Counter

my_path = "ACI_Inventory/json/"
my_file = "delk.json"
my_url = my_path + my_file
output = 'output_' + my_file + '.csv'
my_dict = dict()
my_list = list()

with open(my_url) as f:
    data = json.load(f)

for i in data['imdata']:
    for key in i['dhcpClient']['attributes']:
        if key == 'id':
            serial_num = i['dhcpClient']['attributes'][key]
            my_dict[key] = serial_num

        if key == 'model':
            device = i['dhcpClient']['attributes'][key]
            my_dict[key] = device

    dict_copy = my_dict.copy()
    if dict_copy not in my_list:
        my_list.append(dict_copy)

print(len(my_list))
pprint(my_list)
