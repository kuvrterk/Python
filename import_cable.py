import csv
import nb_auth_dev

header = ['side_a_device.id','side_a_type','side_a_name','side_b_device.id','side_b_type','side_b_name','type','status']
def nb_comparsion(device_hostname, nb):
    
    nb_device = nb.dcim.devices.filter(name=device_hostname)
    #nb_device_count = nb.dcim.devices.count(name=device_hostname)

    for device in nb_device:
        if str(device.site) == 'SSF1':
            return str(device.id)

    return device_hostname
    


def standardization(row, device, nb):
    new_cable_list = []
    console_role_pop = False

    if row == '' or row.find('port ?') != -1:
        return new_cable_list
    #spltting the string to individual strings in a list
    console_row = row.split(' ')

    if len(console_row) < 3:
        return new_cable_list

    if console_row[0] == '#' or console_row[0] == '#rsvd:':
        console_row.pop(0)
        console_role_pop = True

    new_cable_list.append(nb_comparsion(device, nb))
    new_cable_list.append('dcim.consoleserverport')    
    new_cable_list.append('serial-' + console_row[5][0 : len(console_row[5]) - 1])
    #Removing the .SSF1 depending on the string's length
    cable_b_device = console_row[1]
    new_cable_string = cable_b_device.split('.')
    console_row[1] = new_cable_string[0]
    new_cable_list.append(nb_comparsion(console_row[1], nb))
    
    new_cable_list.append('dcim.consoleport')
    new_cable_list.append('console-0')
    new_cable_list.append('cat6')

    if row.find('no response') != -1 or row.find('temp') != -1:
        new_cable_list.append('planned')
    else:
        new_cable_list.append('connected') 

    if row.find('verified') != -1 and row.find('Temp') != -1 or row.find('no response') != -1 or row.find('} #  ') != -1:
        new_cable_list = []

    return new_cable_list

def main(filename):
    device = ''
    out_csv = 'import_cable.csv'
    nb = nb_auth_dev.main_auth()
    with open(out_csv, 'w', newline= '') as output_obj:
        csv_file_writer = csv.writer(output_obj)
        csv_file_writer.writerow(header)

        for row in filename:
            if row.find('# con-') != -1:
                deviceList = row.split() 
                device = str(deviceList[1])          
            new_csv_row = standardization(row, device, nb)

            if new_csv_row != []:
                csv_file_writer.writerow(new_csv_row)
                print(new_csv_row)
            
    filename.close()

if __name__ == '__main__':
    file = open('Console_cabling.txt')
    main(file)