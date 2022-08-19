"""
What this file is additional functions that can be use in the script depending on the user
and if they want to add them into it
"""

#Returns with a list of files with .csv extensions
#Use for mulitple file input
def get_csv_file():
    path = os.getcwd()
    csv_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".csv"):
                path_file = os.path.join(root,file)
                string_path_file = str(path_file)
                string_split = string_path_file.split('/')
                for csv in string_split:
                    csv_files.append(string_split[len(string_split) - 1])
            
    csv_files = list(set(csv_files))
    #print(csv_files)
    return csv_files

#Creates a device type in NB (Note this does not work)
#It prints the HTML/CSS/Javascript of netbox, but can be fixed for future uses
def device_type_creation(nb):

    nb = nb_auth_dev.main_auth()
    get_manuf = input('What is the manufacturer of the device: ')
    get_model = input('What is the model of the device: ')
    get_height = input('What is the height of the device: ')

    try:
        new_device = nb.dcim.device_type.create([
            {
            'manufacturer':     str(get_manuf),
            'model':            str(get_model),
            'slug':             get_model.lower(),
            'u_height':         get_height
            }
        ])
    except pynetbox.RequestError as e:
        print(e.error)

#Creates a description on a device interface
#Needs the device ID (by the for loop, gets the ID), inerface ID, interface, type, and the description
def interface_desc_creation(device_name, nb, site_location)
    device_name = 'fwo-2md-03-01'
    nb = nb_auth.main_auth()
    nb_device = nb.dcim.devices.filter(name=device_name)
    nb_id = 0
    for device in nb_device:
        if str(device.site) == site_location:
            nb_id = device.id
    try:
        interface = nb.dcim.interfaces.update([
            {
            'device': nb_id,
            'id': input('What is the device interface ID'),
            'name': 'ge-0/0/0',
            'type': '1000base-t',
            'enable': True,
            'description':  ''}
        ])
    except pynetbox.RequestError as e:
        print(e.error)
