#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def clear(): 
    """
    Method clears the terminal screen.
    INPUTS: none
    OUTPUT: none
    """
    from os import system, name 
    
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
         


# In[ ]:


def flush_input():
    """
    Method attempts to flush keyboard inputs.
    INPUTS: none
    OUTPUT: none
    """
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


# In[ ]:


def display_dict(dev, indent_count=0):
    """
    Method recursively prints data body containing either dict or list
    INPUTS: none 
    OUTPUT: none
    """
    
    indent = "\t"
    
    if isinstance(dev, dict): 
        
        for k, v in dev.items():
            if isinstance(v, dict):
                if indent_count == 0:
                    print(f"{k}:")
                else:
                    print(f"{indent_count*indent}{k}:")
                
                display_dict(v, indent_count+1)
                
            elif isinstance(v, list):
                if indent == 0:
                    print(f"{k}:")
                else:
                    print(f"{indent_count*indent}{k}:")
                    
                display_dict(v, indent_count+1)
                
            else:
                if indent == 0:
                    print(f"{k} = {v}")
                else:
                    print(f"{indent_count*indent}{k} = {v}")
    
    elif isinstance(dev, list):
        
        for i in range( len(dev) ):
            if indent == 0:
                display_dict(dev[i])
            else:
                display_dict(dev[i], indent_count+1)
        


# In[ ]:


def getline_input():
    """
    Method collects user inputs for phone line number 
    INPUTS: none 
    OUTPUT: Returns int
    """
   
    loop = True
    
    while loop:
        
        line = input("Enter line no. (default=1): ")
        
        if line == "":
            # empty input defaults to 1.
            return 1
        
        if line.isdigit(): 
            if int(line) <= 0:
                print(f"Invalid input '{line}' >> Expecting integer(>=1).")
            else:
                loop = False
        else:
            print(f"Invalid input '{line}' >> Expecting integer(>=1).")            
    
    return int(line)
    


# In[ ]:


def getlinetype_input():
    """
    Method collects user inputs for line type - TEL or SIP 
    INPUTS: none 
    OUTPUT: Returns str
    """
    
    valid_values = ( "TEL", "SIP" )
    loop = True
    
    while loop:
        
        linetype = input(f"Enter line type, {valid_values} (default='TEL'): ")
        
        if linetype == "":
            # empty input defaults to 1.
            return "TEL"
        
        if linetype.upper() in valid_values: 
            loop = False
        else:
            print(f"Invalid input '{linetype}' >> Expecting [{valid_values}].")            
    
    return linetype.upper()    
    


# In[ ]:


def getdest_input(linetype="TEL"):
    """
    Method collects user inputs for destination dialstring - TEL or SIP 
    INPUTS: linetype as str ('TEL' or 'SIP') 
    OUTPUT: Returns str
    """
    import re
       
    loop = True
    
    while loop:
        
        dest = input(f"Enter destination dialstring [{linetype}]: ")
        
        if dest != "":
            
            if linetype == "TEL":
                res = re.match("\d+", dest)
                if res:
                    loop = False
                else:
                    print(f"Invalid input '{dest}' >> Expecting TEL(E.164) dialstring.")
                    
            elif linetype == "SIP":
                res = re.match("([^@|\s]+@[^@]+\.[^@|\s]+)", dest)
                if res:
                    loop = False
                else:
                    print(f"Invalid input '{dest}' >> Expecting SIP URI dialstring.")
                
        else:
            print(f"Empty input '{dest}' >> Expecting {linetype} dialstring.")
    
    return dest
    


# In[ ]:


def getduration_input():
    """
    Method collects user inputs for duration in seconds, minimum value is 0 and maximum value is 600s. Defaults to 0 
    if not inputs from user.
    INPUTS: none 
    OUTPUT: Returns int. 
    """
   
    loop = True
    
    while loop:
        
        duration = input("Enter call duration(s) (default=10): ")
        
        if duration == "":
            # empty input defaults to 10.
            return 10
        
        if duration.isdigit(): 
            if ( int(duration) < 0 ) | ( int(duration) > 600 ):
                print(f"Invalid input '{duration}' >> Expecting integer(0-600).")
            else:
                loop = False
        else:
            print(f"Invalid input '{duration}' >> Expecting integer.")            
    
    return int(duration)
    


# In[ ]:


def getcallhandle_input():
    """
    Method collects user inputs for callhandle as str
    INPUTS: none 
    OUTPUT: Returns int. 
    """
   
    loop = True
    
    while loop:
        
        callHandle = input("Enter callHandle: ")
        
        if duration == "":
            # empty input defaults to 10.
            return 10
        
        if duration.isdigit(): 
            if ( int(duration) < 0 ) | ( int(duration) > 600 ):
                print(f"Invalid input '{duration}' >> Expecting integer(0-600).")
            else:
                loop = False
        else:
            print(f"Invalid input '{duration}' >> Expecting integer.")            
    
    return int(duration)
    


# In[ ]:


def getconfirmation_input(action):
    """
    Method collects user confirmation to proceed with action 
    INPUTS: action as str, description of the action 
    OUTPUT: Returns boolean, True to proceed, False to not proceed.
    """
    loop = True
    
    while loop:
        
        user_input = input(f"Confirm to proceed with '{action}'? [y/N]: ")
        
        if (user_input == "Y") | (user_input == "y"):
            return True
        elif (user_input == "") | (user_input == "N") | (user_input == "n"): 
            return False
        else:
            print(f"Invalid input '{user_input}' >> Expecting [y/Y/n/N].")                
    


# In[ ]:


def connect_device(module_version, username="Polycom", password="789"):
    """
    Method collects user inputs for phone's IP address, username and password
    INPUTS: none 
    OUTPUT: Returns result as list, [ ip, (username, passwd) ]
    """
    import ipaddress
    
    ip = ""
    loop = True
    
    print(f"Welcome to VVXME CLI Menu version {module_version}\n")

    while loop:            
        try:
            ip = ipaddress.ip_address( input("Enter IP address of the phone: ") )
            print(f"{ip} is a valid IP{ip.version} address")
            loop = False
        except ValueError as err:
            print(f"Value Error: <{err}>")


    usr = input(f"Enter username(Default: '{username}') :")
    if usr != "":
        username = usr

    pwd = input(f"Enter password(Default: '{password}'): ")
    if pwd != "":
        password = pwd

    return [ip.exploded, (username, password)]


# In[ ]:


def pdmssp_connect_device(module_version):
    """
    Method collects user inputs for phone's MAC address.
    INPUTS: none 
    OUTPUT: Returns macaddr when successful, None when unsuccessful.
    """
    import re

    print(f"Welcome to VVXME CLI Menu version {module_version}\n")
    print("Attempting to connect endpoint on PDMS-SP:\n")
    print("[Step-1]: Collect phone MAC Address.\n")
                    
    macaddr = ""
    loop = True 
    
    while loop:            
        macaddr = input("Enter MAC address of the phone(no separators[-:], Eg.64167f12a34b): ")

        if re.match("([0-9a-f]{2}){6}$", macaddr.lower()):
            print(f"{macaddr} is a valid MAC address.")
            return macaddr
        
        else:
            print(f"Invalid input '{macaddr}' >> Invalid MAC address format. Do not use separators[-:], Eg.64167f12a34b")
    


# In[ ]:


def pdmssp_configfile_parser(module_version):
    """
    Method attempts to parse pdmssp config file for client_id, client_secret and org_id. 
    *NOTE1: config file is expected to live in HOME directory, with default name as 'pdmssp.cfg'
        Syntax of config file:
                            [API_KEY]
                            client_id = <xxxxx>
                            client_secret = <xxxx>
                            
                            [ORG]
                            org_id = <xxx>
    *NOTE2: Environment variable 'HOME' containing the folder location has be created in Windows OS.                        
    INPUTS: absolute_path as str, filename as str.
    OUTPUT: Returns result as dict when parse is successful, None when parse fails.
    """   
    import configparser
    
    print("\n[Step-2]: Retrieve client_id, client_secret and org_id from config file.")
    print("***NOTE: Expecting config file to live in folder defined in HOME environment variable!***\n")
          
    filename = input(f"Enter config filename (default='pdmssp.cfg'): ")
    if filename == "":
        filename = 'pdmssp.cfg'
   
    from pathlib import Path
    home_path = Path.home()
          
    if not home_path:
        print(f"\nHome folder not found!: {str(home_path)}") 
        return
          
    cfgfile = home_path/filename

    if not cfgfile.exists():
        print(f"\nFile not found!: {str(cfgfile)}")
        return
    
    body = {}
    
    try:
        config = configparser.ConfigParser()
        config.read(cfgfile)    

        body["client_id"] = config["API_KEY"]["client_id"]
        body["client_secret"] = config["API_KEY"]["client_secret"]
        body["org_id"] = config["ORG"]["org_id"]

        return body      
        
    except KeyError as key_err:
        print(f"\nKeyError Exception: {key_err}")
        input("\nPress Enter to continue...")
    except configparser.Error as err:
        print(f"\nException: {err}")
        input("\nPress Enter to continue...")


# In[ ]:


def ucs_configfile_parser(filename="import.cfg"):
    """
    Method attempts to parse input 'filename' as XML first. Upon XML parse failure, attempt next to parse as JSON.
    Method doesn't cater for absolute path+name, expects 'filename' to exists in current folder only.
    XML Body: uses standard VVX/UCS syntax. Does not parse Root Element.
    JSON Body: expects UCS RestAPI body, eg. { 'data' : { 'parameter1' : 'value1', 'parameter2' : 'value2', ... } }
    INPUTS: filename as str, expect to be existent no further filename checks.
    OUTPUT: Returns result as dict when parse is successful, None when parse fails.
    """
    
    import json
    import xml.etree.ElementTree as ET
    import time
    
    params_dict = {}
    body_dict = {}
    
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        for child in root:
            for sub in child.iter():
                if sub.attrib:
                    for k, v in sub.attrib.items():
                        params_dict[k] = v
        
        body_dict["data"] = params_dict
        print("")
        print("Parse XML Success!")
        print("==================")
        return body_dict
           
    except ET.ParseError as xml_err:
        print(f"[XML] Parse Error: <{xml_err}>\n")
        print("Trying to parse JSON now...\n")
        #input("Press Enter to continue...")

        try:
            with open(filename, 'r') as f:
                params_dict = json.load(f)
                body_dict = params_dict
                print("")
                print("Parse JSON Success!")
                print("===================")
                return body_dict
                
        except ValueError as json_err:
            print(f"[JSON] Parse Error: <{json_err}>\n") 
            print("Failed parse JSON too. Please try again...\n")
            input("Press Enter to continue...")
            return
            

