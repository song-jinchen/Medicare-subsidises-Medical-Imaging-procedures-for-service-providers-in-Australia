import logging
from utils.config_logging import config_logging

config_logging()
def handle_exceptions(group,subgroup,value,td_values):
    # Special case for Group: I2 Computerised Tomography, Subgroup: 10 Pelvimetry
    logging.info("Special case for Group: I2 Computerised Tomography, Subgroup:")
    if group == 'I2 Computerised Tomography' and subgroup == '10 Pelvimetry':
        td_values.insert(5, '0')  
        
    if group == 'I3 Diagnostic Radiology' and subgroup == '14 Tomography' :
        
        for _ in range(7): 
            td_values.insert(1, '0') 
    if value == 'I0316' :
            for _ in range(7):  
                td_values.insert(0, '0')
    if value == 'I0516' :
        for _ in range(2):  # Insert '0' seven times
            td_values.insert(2, '0')
    if value == 'I0517' :
        for _ in range(3):  # Insert '0' seven times
            td_values.insert(1, '0')
    return td_values