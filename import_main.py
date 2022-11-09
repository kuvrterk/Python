#!/usr/local/bin/python3
import csv
import pynetbox                     #importing netbox library 
from deviceDictionary import *
from nb_listcalls import *          #calls all functions in the 'nb_listcalls.py' to set the list in gloabl functions

#This is a global variable that sets the header for the outout csv file 
header = ['site', 'location', 'rack', 'position', 'face', 'manufacturer', 'device_type', 'name', 'status', 'device_role', 'tenant', 'comments']
rack_group = rack_group_list()      #1ie-01
location = location_list()          #1ie
site = ['SSF1']                     #SSF1       #sites_list()
manufactruer = manufactruer_list()
model_name = device_model_list()
device_role = device_role_group()
active_Junipter_list = active_devices()
#set to 0 that way it'll be zero when the fucntion occurs
counter = 0
rack_location = ''

#global counter to determine which rack_group is needed
#returns a int
def incerment():
    global counter
    counter += 1

    return counter

#Arugment is a 3 char string (location) 1le
#return the a string as 1ie-01 for example
def location_incerment(location_input):

    incerment()
    #Finding out how many racks are there within the site
    newString = location_input + '-' + '0' + str(counter)
    return newString

""""
#agurment is two strings
#returns a string
#converts a string to a int then subtract the U depending on the size
#Checks if the string can be convertable or returns cell and does nothing
#2u -> -1 tp unit, 3U -> -2
#Netbox puts the device at the btoom then up, if it was place in 32 in csv, then the bottom is at 32
#And the top would be at unit 33
"""
def uConversion(cell, unitPDU):
    if cell == '0L' or cell == '0R':
        return ''
    
    if not cell.isdigit():
        return cell

    for key in unitPDUDict:
        if unitPDU == key:
            cellNumber = int(cell)
            cellNumber = cellNumber - unitPDUDict[key] + 1
            cell = str(cellNumber)
            return cell
    
    return cell

#Agurment is a list
#return is a empty list or dow nothing
#Function checks if there is enough blink spaces to delete the row
#Netbox does not like having rows with no information in them
def emptyRow(new_csv_row):
    rowCounter = 0

    for cells in new_csv_row:
        if cells == '':
            rowCounter += 1
    
    if rowCounter > 3:
        return new_csv_row.clear()
    
    return new_csv_row


#Arugment is a string (hostname of the device) and another string (status of the device)
#third is the third cell in the csv row
#Return would be a string (device role)
#function is comparing the name of the device with the dictionary to determine
#the role of the device, while comparing plannaed device to get the device role
#name of the device, device status, and csv_row[3]
def device_type(device_role, csv_row):

    #only having the first three letters to compare
    device_role = device_role[0:3]

    #comparing with first dictory if it was a hostname
    for key in deviceDict:
        if device_role == deviceDict[key]:
            return key

    #comparing with first dictory with no hostname and if a value is in the string
    for key in deviceDict:
        for value in csv_row:
            if value.find(key) != -1:
                return key

    #comparing with second dictory ti manual check for a value
    for key in potentialFuture:
        for value in csv_row:
            if value.find(key) != -1:
                return potentialFuture[key]

#comparing csv_row and list to determine the status of the string
#Arugment: host name and csv row
#return is status string
def device_status(device_name, csv_row):

    #checking for specified words in the csv file
    for value in csv_row: 
        if(value.find('Future') != -1) or (value.find('Rvsd') != -1):
            return 'planned'
    #checking for remove word in csv
    for value in csv_row:
        if(value.find('remove') != -1):
            return 'decommissioning'
    
    #checking for other active that doesn't have hostnames
    if csv_row[1] != '' and csv_row[1] != 'N/A' and csv_row[1] != 'MT':
        return 'active'

    #checking for devices that aren' listed, but have hostnames
    if(device_name != ''):
        return 'active'

    #If it has no hostnames
    if(device_name == ''):
        return ''

  #Checking the list first to make sure the device is active
    for devices in active_Junipter_list:
        if(devices.find(device_name) != -1):
            return 'active'
    
#checks the model name for the deivce
#Arugment is a list (a single row from the csv file that's a string)
#returns a string
def model_name_pair(csv_row):
    device_model = ''
    
        
    for device in model_name:                   
        for value in csv_row:                                   
            #Check if the row string excatly matches a device name in model_name
            if(value.find(device) != -1):
                device_model = device
                return device_model

            #Manually checking model name of the device if not listed in the list
            if (value.find('EX4300P') != -1):
                device_model = model_name[model_name.index('EX4300-48P')]
                return device_model
            elif (value.find('EX4300T') != -1):
                device_model = model_name[model_name.index('EX4300-48T')]
                return device_model
            elif (value.find('EX4300MP') != -1):
                return 'EX4300-48MP'
            elif (value.find('RJ45') != -1) and (value.find('2U') != -1):
                return 'copper-2u-48ports'
            elif (value.find('RJ45') != -1) or (value.find('1U') != -1) or (value.find('R45')) != -1:
                return 'copper-1u-24ports'
            elif (value.find('Leviton') != -1) and (value.find('24') != -1):
                return 'copper-1u-24ports'
            elif (value.find('Leviton') != -1) and (value.find('48') != -1):
                return 'copper-2u-48ports'
            elif (value.find('Copper') != -1) and (value.find('24') != -1):
                return 'copper-1u-24ports'
            elif (value.find('Copper') != -1) and (value.find('48') != -1):
                return 'copper-2u-48ports'    
            elif (value.find('SRX-4600') != -1):
                return 'SRX4600'
            elif (value.find('Wire Manager Panel') != -1):
                return 'WMP'
            elif (value.find('fiber') != -1) and value.find('8') != -1:
                return 'fiber-1u-3x8ports'
            elif (value.find('fiber') != -1) or value.find('12') != -1 or (value.find('Patch Panel') != -1):
                    return 'fiber-1u-3x12ports'
            elif (value.find('Avocent')) != -1 and (value.find('32')) != -1 or value.find('ACS8032') != -1:
                return 'ACS8032'
            elif (value.find('Avocent')) != -1 and (value.find('48')) != -1 or value.find('ACS8048') != -1:
                return 'ACS8048'
            elif (value.find('Avigilon')) != -1 and (value.find('2U') != -1):
                return 'NVR-2U'
            elif (value.find('Avigilon')) != -1 and (value.find('1U') != -1):
                return 'NVR-1U'
            elif (value.find('Aruba')) != -1 and (value.find('7210') != -1):
                return '7210'
            elif (value.find('swa-')) != -1:
                return 'EX4300-48P'
            elif (value.find('pat-')) != -1:
                return 'copper-1u-24ports'
            elif (value.find('Quanta')) != -1 and (value.find('1u')) != -1:
                return 'D51B-1U'
            elif (value.find('Supermicro')) != -1 and (value.find('thp')) != -1:
                return 'SYS-1029U-E1CRT'
            elif (value.find('PA-5260')) != -1 and (value.find('fw')) != -1:
                return 'PA-5260'
            elif (value.find('Dell')) != -1 and (value.find('vhp')) != -1:
                return 'PowerEdge R640'
        
    return device_model

#Arugument is a list
#returns a string
#Loops throughout the list (row) until if finds the device manufracter type
def manufactruer_pair(csv_row):
    manufactruer_value = ''
    for device in manufactruer:
        for values in csv_row:
            if(values.find(device) != -1): 
                return device 
            elif (csv_row[3] == '' and csv_row[2] == ''):  
                manufactruer_value = ''
            else:
                manufactruer_value = 'unspecified'

    #Manuelly checks the dictory to see if a hostname is only listed in the csv
    #Then checks the dictory to see if they match up
    #This condition is only for devices with no information other then hostname listed
    for key, values in manuDict.items():
        for cell in csv_row:
            for keyValue in values:
                if cell.find(keyValue) != -1:
                    return key
   
    return manufactruer_value
        

#csv_row = row (list objective)
#Returns a list 
def check_csv_cell(csv_row, location_input):
    #checking if the rack name has changed
    global rack_location
    
    if csv_row[0] == '48':
       rack_location = location_incerment(location_input)

    new_csv_row = []
    
    new_csv_row.append(site[0])
    new_csv_row.append(location_input)
    new_csv_row.append(rack_location)

    #decrement the U number for and place it in the csv row
    #getting the model name to decrement the unit
    unitPDU = model_name_pair(csv_row)
    new_csv_row.append(uConversion(csv_row[0], unitPDU)) 
    #if there is N/A, but there is a hostname, then it'' return front
    if (csv_row[1] == 'N/A' and csv_row[2] == '') or csv_row[1] == '':
        new_csv_row.append('')
    else:
        new_csv_row.append('front')
    
    #Finding the device type and placing it in the csv value
    new_csv_row.append(manufactruer_pair(csv_row))
    
    #model name right here
    new_csv_row.append(unitPDU)
   
    #hostname of the device
    if csv_row[2] == '':
        new_csv_row.append("")
    else:
        new_csv_row.append(csv_row[2])
    
    #status of the device
    new_csv_row.append(device_status(csv_row[2], csv_row))

    #Get the device role
    new_csv_row.append(device_type(csv_row[2], csv_row))

    #check to determine if it a ISP
    if (csv_row[1] == 'CenturyLink'):
        new_csv_row.append('Other')
        new_csv_row.append('CenturyLink')
    else:
        new_csv_row.append('')
      

    #Comment section of the csv file
    if csv_row[0] == '0L':
        new_csv_row.append('Left')
    elif csv_row[0] == '0R':
        new_csv_row.append('Right')
    else:  
        new_csv_row.append('')

    return new_csv_row
   
#Main function for CSV file
#2 arguments: both are string file objects that open up the csv file
def main(csv_file, out_csv):      
    with open(out_csv, 'w', newline= '') as output_obj:
        with open(csv_file) as file_obj:
            csv_file_reader = csv.reader(file_obj)
            csv_file_writer = csv.writer(output_obj)

            location_input = input('Enter site location (1ie for example): ')
            #userInputValidation(location_input)
            #writes header into the output csv file
            csv_file_writer.writerow(header)

            #literate through every row in the csv and format to netbox's liking
            for row in csv_file_reader:
                new_csv_row = check_csv_cell(row, location_input)
                print(new_csv_row)
                #clearing out rows with no information in them
                emptyRow(new_csv_row)

                if new_csv_row != []:
                    csv_file_writer.writerow(new_csv_row)
       

#User enters the csv they want to standardize for netbox
if __name__ == '__main__':
    #csv_file = input('Enter CSV file to standardize: ')
    csv_file = 'SSF1 Rack Layouts 2md.csv'
    out_csv = 'test.csv'
    #csv_file = input("Enter the CSV file: \n")
    main(csv_file, out_csv) 

