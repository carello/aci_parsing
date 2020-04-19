
import json

template = '{0:20} {1:20}'

my_path = "ACI_Inventory/json/"
my_file = "lc_lab.json"
my_url = my_path + my_file
output = 'output_' + my_file + '.csv'


def headers():
    print('\n' + (template.format('SERIAL', 'MODEL')))
    print('-' * 40)


def open_file():
    with open(my_url) as f:
        data = json.load(f)
    return data

def get_info(data):
    my_dict = dict()
    my_list = list()
    for i in data['imdata']:
        for key in i['dhcpClient']['attributes']:
            if key == 'id':
                my_dict[key] = i['dhcpClient']['attributes'][key]

        for key in i['dhcpClient']['attributes']:
            if key == 'model':
                my_dict[key] = i['dhcpClient']['attributes'][key]

        dict_copy = my_dict.copy()
        if dict_copy not in my_list:
            my_list.append(dict_copy)
    return my_list

def view(r):
    print(len(r))
    headers()
    for i in r:
        print(template.format(i['id'], i['model']))

def save_file(r):
    with open(output, 'a') as do:
        do.writelines(["TOTAL: ", str(len(r)),'\n'])
        do.write('\n')
        for thing in r:
            do.writelines([thing['id'], ',', thing['model']])
            do.write('\n')
        do.write('\n')

result = get_info(open_file())
view(result)
save_file(result)
