import pynetbox
import nb_auth_dev

nb = nb_auth_dev.main_auth()

#returns the list of manufactruers in netbox
def manufactruer_list():
    
    manu_list = []
    netbox_manufactruer_list = nb.dcim.manufacturers.all()
    
    #converts record value into a string list value
    for device in netbox_manufactruer_list:
        manu_list.append(str(device))

    return manu_list

#return the list of current device model in netbox
def device_model_list():
   
    device_list = []
    netbox_device_list = nb.dcim.device_types.all()

    for device in netbox_device_list:
        device_list.append(str(device))

    return device_list

#Returns the list of current
def rack_group_list():

    rack_group = []
    netbox_rack_list = nb.dcim.racks.all()

    for rack in netbox_rack_list:
        rack_group.append(str(rack))
    
    return rack_group

def location_list():

    location_group = []
    netbox_location_list = nb.dcim.locations.all()

    for location in netbox_location_list:
        location_group.append(str(location))
    
    return location_group

def sites_list():

    sites_group = []
    netbox_sites_list = nb.dcim.sites.all()

    for sites in netbox_sites_list:
        sites_group.append(str(sites))
    
    return sites_group

def device_role_group():
 
    device_group = []
    netbox_sites_list = nb.dcim.device_roles.all()

    for device in netbox_sites_list:
        device_group.append(str(device))
    
    return device_group

#opens up the file, read the values from the file, then strip the '\n'
#from the end of each list string element
def active_devices():
    converted_list = []      
    txt_file = open('active_junipter.txt', "r")
    content_list = txt_file.readlines()
    txt_file.close()

    for devices in content_list:
        converted_list.append(devices.strip())

    return converted_list
""""
API Call that gets the device details, if needed in the furture here's an example
nb = nb_auth_dev.main_auth()
device_name_ko = 'srv4305'
nb_device = nb.dcim.devices.filter(name=device_name_ko)
nb_device_count = nb.dcim.devices.count(name=device_name_ko)

print(nb_device_count)
for device in nb_device:
        hostname = str(device.name)
        device_id = str(device.id)
        device_site = str(device.site)

        if device_site == 'SSF1':
         print(hostname + ' ' + device_id + ' ' + device_site)
"""