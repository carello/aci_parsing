
from abc import ABC, abstractmethod
import json

my_path = "ACI_Inventory/json/"
my_file = "lc_lab.json"
my_url = my_path + my_file
output = 'output_' + my_file + '.csv'


def open_file():
    with open(my_url) as f:
        aci_data = json.load(f)
    return aci_data


class Abbott(ABC):
    @abstractmethod
    def get_info(self):
        raise NotImplementedError


class ACI(Abbott):
    def __init__(self, data):
        self.data = data
        self.my_dict = dict()
        self.my_list = list()

    def get_info(self):
        for i in self.data['imdata']:
            for key in i['dhcpClient']['attributes']:
                if key == 'id':
                    self.my_dict[key] = i['dhcpClient']['attributes'][key]

            for key in i['dhcpClient']['attributes']:
                if key == 'model':
                    self.my_dict[key] = i['dhcpClient']['attributes'][key]

            dict_copy = self.my_dict.copy()
            if dict_copy not in self.my_list:
                self.my_list.append(dict_copy)
        return self.my_list


class View(object):
    def __init__(self, rr):
        self.rr = rr
        self.template = '{0:20} {1:20}'

    def headers(self):
        print('\n' + (self.template.format('SERIAL', 'MODEL')))
        print('-' * 40)

    def view(self):
        print(len(self.rr))
        self.headers()
        for i in self.rr:
            print(self.template.format(i['id'], i['model']))

    def save_file(self):
        with open(output, 'a') as do:
            do.writelines(["TOTAL: ", str(len(self.rr)), '\n'])
            do.write('\n')
            for thing in self.rr:
                do.writelines([thing['id'], ',', thing['model']])
                do.write('\n')
            do.write('\n')


def main():
    r_data = open_file()
    yo = ACI(r_data)
    see = View(yo.get_info())
    see.view()
    see.save_file()


if __name__ == "__main__":
    main()
