# Netbox Import Scripts

## Overview

These scripts are use for importing devices and device cabling into netbox. This is done by using netbox python library call `pynetbox` and inbult library `csv`. Each script folder has a producation and development authentication folder depending on the useage. Also, each folder would a csv or txt file as an example on how to accurately standardize the csv for the script to work.

## Pynetbox library

`pynetbox` is a open source library for netbox that can be find in this public [pynetbox](https://github.com/netbox-community/pynetbox) repo.

### Installtion

To install the library you need to run the `pip install pynetbox`, `sudo` may need to be added.

Or you can clone the repo and run `python setup.py install`.

When creating a python script with the library make sure to have `import pynetbox` in it.

## Documentation 

There are servally documentation I found throughout researching netbox, here is some that I found and could be useful.

* [Main doc](https://pynetbox.readthedocs.io/en/latest/), tells you the how to use the library to access the `REST API` for netbox.
* [Extended doc](https://pynetbox.readthedocs.io/_/downloads/en/latest/pdf/) for a more detail way of using the library as a downloadable PDF file.
* [Netbox REST API](https://netbox.techops.us-west-2.dev.23andme.net/api/docs/) is the doc for the actually `REST API` for netbox that is in a JSON format. Note that `pynetbox` uses parameters from the `JSON` version into the library to call the API. Note, you can only access this by a VPN or on the company network.
* [Netbox REST API doc](https://docs.netbox.dev/en/stable/) and how netbox works in detail. If wanting to work with the actually `REST API`, this is the perfect doc for you. Also, [ttam-netbox/utils](https://github.com/23andme-private/ttam-netbox/tree/master/utils) has example working with the `REST API`

## Token Authentication

Before you can run the scripts you must create a API token for your account on netbox. Note, that you must create two tokens for production and development servers. 
* Go to [Netbox dev](https://netbox.techops.us-west-2.dev.23andme.net/) or [Netbox prod](https://netbox.techops.us-west-2.prd.23andme.net/).
* Go to your account (email) -> profile -> API token -> add a token.
* You can create your API token in the box, if none is presented then netbox would create one for you.
* Hit the create button and the API token is created.

You can also use `pynetbox` to create an API token listed in the docs.

## Using the Scripts

Please note that the outputted information is according to netbox's liking and the hostname would disappear in favor of the device id. If there is no id, the device has not been entered inside of netbox. Also, the outputted information would be in a csv file to copy directly from while printing to the terminal.

### Device import

For the script to run properly you must format the CSV into three columns according;

rack U number |  manufacture/device model | hostname    | Additional infomation or  comments|
--------------|---------------------------|-------------|-----------------------------------|
48            |       EX4300MP-48         |swa-2iw-01-01| Juniper EX4300MP switch - 48 ports|

The fourth column could be a wildcard column if you choose to add that, but it is not needed. The script can determine the correct output based on the three column alone. Note that by default it would have a status of active, unless a reserve word like 'Reserved' is added in the second column or in the row in general.

### Cable import

Their are three different cable scripts depending on how the information is being feed into the script. One of them is for a .txt file and the other is for a csv file. 

#### TXT file

For the .txt script for work you must format the file accordingly;

(# con-1ie-02-01

console con-1ie-01-01.ssf1	{ include con-1ie-02-01.ssf1; port 02; } # verified 2020-09-11

Must have the device type a in # hostname -> next line -> device type b host name followed by verifed (it is active) or # blinke or no reponse, then the status os not active. This is meant for devices that are connecting to the console server ports.

#### CSV file

For import of the cabling via .csv file you must format the csv accordingly;

row 1:    blink          | device a hostname | device a hostname | device a hostname | etc for how many device
-------------------------|-------------------|-------------------|-------------------|-
row 2: device a interface|device b hostname. | device b hostname.| device b hostname.| etc

Note if there is no connection then leave blink. Note the device b hostname must have a . or : at the end of it. If connecting the interface to a port on device b then device b hostname must have an : followed by the interface. So for example device b is `dsw251:xe-0/2/1`, then it's hostname:interface. If the interface is a managment port, then put .pM at the end of it.

#### Utility functions

I have added an aditional functions for netbox such as API authentication for prod or dev server and additional funtions that can swap added to make life more easier.