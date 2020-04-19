
import json
from collections import defaultdict, Counter
from pprint import pprint

my_file = "seeme.json"
my_path = "ACI_Inventory/json/"
my_url = my_path + my_file
output = 'output_' + my_file

my_dict = defaultdict()

with open(my_url) as f:
    data = json.load(f)

with open(output, 'a') as d:
    d.writelines(["TOTAL COUNT: ", data["totalCount"], '\n'])
    d.write('\n')

def get_info():
    for i in data['imdata']:
        for key in i['dhcpClient']['attributes']:
            if key == 'model':
                device = i['dhcpClient']['attributes'][key]
                #my_dict.update({key: device})

            if key == 'id':
                serial_num = i['dhcpClient']['attributes'][key]
                #my_dict.update({key: serial_num})

        my_dict[serial_num][device]
    return my_dict

pprint(get_info())


'''        
    with open(output, 'a') as do:
        for k, v in sorted(my_dict.items()):
            do.writelines([k, ': ', v])
            do.write('\n')
        do.write('\n')
    print()
'''