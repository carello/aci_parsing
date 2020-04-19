import untangle

my_path = "ACI_Inventory/xml/"
my_file = "lc_lab.xml"
my_url = my_path + my_file
output = 'output_' + my_file + '.csv'

template = '{0:10} {1:20} {2:15} {3:15} {4:15}'

def get_data():
    obj = untangle.parse(my_url)
    tot_rows = obj.imdata['totalCount']
    tot_rows = int(tot_rows)
    return tot_rows, obj

def headers():
    print('\n' + (template.format('NODE', 'MODEL', 'SERIAL', 'STATUS', 'IP')))
    print('-' * 82)
    return

def out_put(nd_list, serial_items, node_items):
    #nd_list.sort()
    for x in set(nd_list):
        print((template.format(*x)))

    print("\nDevice count by Serial_num: {0}".format(len(serial_items)))
    print("Device count by Node_id: {0}\n".format(len(node_items)))

def main():
    t_row, obj = get_data()
    serial_items = set()
    node_items = set()
    nd_list = []
    count = 0
    headers()
    while count < t_row:
        if obj.imdata.dhcpClient[count]['model'] != "N9K-C9508":
            dev_serial = obj.imdata.dhcpClient[count]['id']
            dev_ip = obj.imdata.dhcpClient[count]['ip']
            node_id = obj.imdata.dhcpClient[count]['nodeId']
            client_event = obj.imdata.dhcpClient[count]['clientEvent']
            model_type = obj.imdata.dhcpClient[count]['model']
            tmp_list = node_id, model_type, dev_serial, client_event, dev_ip
            nd_list.append(tmp_list)
            serial_items.add(dev_serial)
            node_items.add(node_id)
        count += 1
    out_put(nd_list, serial_items, node_items)
    print(serial_items)
    print(node_items)
    print(nd_list)
    return


if __name__ == '__main__':
    main()
