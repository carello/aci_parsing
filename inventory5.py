#!/usr/bin/env python3

from abc import ABC, abstractmethod
import json
from operator import itemgetter

my_path = "ACI_Inventory/json/"
my_file = "lc_lab.json"
my_url = my_path + my_file
output = 'output_' + my_file + '.csv'


class OpenFile:
    def __init__(self):
        self.__content = my_url
        self.__data = None

    def open_file(self, __content):
        with open(__content) as f:
            self.__data = json.load(f)
        return self.__data


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


class Mgmt(ABC):
    @abstractmethod
    def view(self):
        raise NotImplementedError

    @abstractmethod
    def save_file(self):
        raise NotImplementedError


class View(Mgmt):
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
        print()
        get_serial_model = itemgetter('id', 'model')
        for i in self.rr:
            print(get_serial_model(i))


    def save_file(self):
        with open(output, 'a') as do:
            do.writelines(["TOTAL: ", str(len(self.rr)), '\n'])
            do.write('\n')
            for thing in self.rr:
                do.writelines([thing['id'], ',', thing['model']])
                do.write('\n')
            do.write('\n')


def main():
    r_data = OpenFile()
    result = r_data.open_file(my_url)

    #r_data = open_file(my_url)
    yo = ACI(result)
    see = View(yo.get_info())
    see.view()
    #see.save_file()


if __name__ == "__main__":
    main()
