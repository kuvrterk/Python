deviceDict = {
    'Building Security':            'bld',        
    'Console Server':               'con',                        
    'Firewall - Core':              'fwc',                
    'Firewall - Out-of-Band':       'fwo',         
    'Firewall - Unwanted':          'fwu',            
    'Other':                        'oth',                                 
    'Patch Panel':                  'pat',                         
    'PDU':                          'pdu',                                 
    'Router - Edge':                'rte',                   
    'Server':                       'srv',                          
    'Storage System':               'sts',                 
    'Switch - Access':              'swa',                 
    'Switch - Core':                'swc',                         
    'Switch - Encryption':          'swe',            
    'Switch - Management':          'swm',                  
    'Switch - Top-of-Rack':         'swt',            
    'UPS':                          'ups',                                 
    'WAP Controller':               'wlc',                 
    'Wireless Access Point':        'wap',           
    'Wire Management Panel':        'wmp'               
}

#This helper dict is for future use to add on
#Adding the device type with other devices that are in the future
potentialFuture = {
    'EX4300P':                      'Switch - Access',
    'Wire Manager Panel':           'Wire Management Panel',
    'Avigilon':                     'Server',
    'WMP':                          'Wire Management Panel',
    'KVM':                          'Other',
    'fw':                           'Firewall - Core',
    'fpp':                          'Patch Panel',
    'wpp':                          'Patch Panel',
    'thp':                          'Server'   
}

#Helper Dict that checks for manuifcater type not listed in the list
#checks for hostanme, if hostname is the only ones given
#Other manufactors can be added in the furture if needed
#MUST BE LIST KEYS for it to work
manuDict = {
    'Juniper':                      ['swa', 'swc', 'swe', 'swm', 'swt', 'fw4'],
    'PAN':                          ['PA-', 'fw-'],
    'Super Micro':                  ['Supermicro', 'Super-mirco']
}

#Helper Dict that has devices that has more then 2U
#Can be replace with accessing netbox API for device unit length
unitPDUDict = {
    'SRT5KRMXLT':                   3,
    'PA-5260':                      3,
    'SRT3000RMXLT':                 2,
    'SMX1500RM2U':                  2,
    'PAN PA-3220':                  2,
    'copper-2u-48ports':            2,
    'CSE-217HQ+-R2K20BP3':          2,
    'FlashBlade-Chassis':           4,
    'NVR-2U':                       2,
    'other-2u':                     2,
    'other-3u':                     3,
    'other-4u':                     4,
    'other-5u':                     5,
    'other-6u':                     6,
    'other-7u':                     7
}